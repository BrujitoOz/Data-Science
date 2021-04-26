x = c(14,7,13,12,16,14,18,13,12,16,13)
y = c(16,12,13,14,15,12,16,11,13,18,17)

#####
regresion <- function(x,y, nx=NA, ny=NA) {
  resultado <- list()
  prediccion <- NA
  n <- NROW(x)
  promX <- mean(x)
  promY <- mean(y)
  (dx <- x - promX)
  (dy <- y - promY)
  (xy <- dx*dy)
  # calculo de la covarianza
  cov <- sum(xy)/(NROW(x)-1) # sentido posi o nega, posi: los dos aumentan o disminuyen - negativo: uno aumenta y otro disminuye
  dx2 <- dx^2
  dy2 <- dy^2
  # calculo de las desviaciones estandar
  sdX <- sqrt(sum(dx2)/(n-1))
  sdY <- sqrt(sum(dy2)/(n-1))
  # calculo del coeficiente correlacional >0.75 aceptable
  (r <- cov/(sdX*sdY)) 
  # creando la prediccion regresional x-y
  if (is.na(ny))
  prediccion <- promY + cov * (nx-promX) / (sdX^2)
  # creando la predeccion regresional y-x
  if (is.na(nx))
  prediccion <- promX + cov * (ny - promY) / (sdY^2)
  
  resultado[[1]] <- data.frame(x,y,dx,dy,xy,dx2,dy2)
  resultado[[2]] <- cov
  resultado[[3]] <- r
  resultado[[4]] <- prediccion
  return (resultado)
}
regresion(x,y,7)
regresion(x,y,NA,16)[[4]]
plot(x,y)
############################
plot(women)
women
regresion(women$height, women$weight, 60) #regresion(women$height, women$weight, ny = 139)



lm(x~y)
# intercepto - pendiente


####################33
plot(mtcars)
install.packages("corrplot")
library(corrplot)
M <- cor(mtcars)
corrplot(M)
cor(mtcars$hp, mtcars$disp)

f = lm(mtcars$mpg~mtcars$hp) #lm(mpg~hp, data = mtcars)
plot(mtcars$hp, mtcars$mpg)
abline(f)
summary(f)
# Regresiones lineales multiples
plot(mtcars)
# obtener la rl de mpg en funcion de disp, hp, drat, wt
f = lm(mpg~disp+hp+drat+wt, data = mtcars)
# predecir en funcion de f

# tecnicas para predecir entrenamiento, pruebas, validacion

# Dataset 100 registros, tuplas, observaciones
# Entrenamiento 50% -> 50
# Pruebas 30% -> 30
# Validar 20% -> 20

# entrenamiento 70% 70
# pruebas 30% 30

ids <- sample(1:NROW(mtcars), NROW(mtcars)*0.7)
entrenamiento <- mtcars[ids, c(1,3:6)]
probar <- mtcars[-ids, c(1,3:6) ]
# generar un modelo para entrenamiento
ft = lm(mpg~disp+hp+drat+wt, data = entrenamiento)
ft1 = lm(mpg~disp+hp+wt, data = entrenamiento)
ft2 = lm(mpg~hp+drat+wt, data = entrenamiento)
# predecir
probar$prediccion <- predict(ft2,probar)
probar

# determinar la precision del modelo entrenado

mean(abs(100*(probar$prediccion-probar$mpg)/probar$prediccion))
# acuracy 100 - 17.31067


# Tarea: Regresion con gradiente descendente

attach(mtcars)
plot(disp, mpg, col = "blue", pch = 20)

model <- lm(mpg ~ disp, data = mtcars)
coef(model)

y_preds <- predict(model)
abline(model)

errors <- unname((mpg - y_preds) ^ 2)
sum(errors) / length(mpg)

gradientDesc <- function(x, y, learn_rate, conv_threshold, n, max_iter) {
  plot(x, y, col = "blue", pch = 20)
  m <- runif(1, 0, 1)
  c <- runif(1, 0, 1)
  yhat <- m * x + c
  MSE <- sum((y - yhat) ^ 2) / n
  converged = F
  iterations = 0
  while(converged == F) {
    ## Implement the gradient descent algorithm
    m_new <- m - learn_rate * ((1 / n) * (sum((yhat - y) * x)))
    c_new <- c - learn_rate * ((1 / n) * (sum(yhat - y)))
    m <- m_new
    c <- c_new
    yhat <- m * x + c
    MSE_new <- sum((y - yhat) ^ 2) / n
    if(MSE - MSE_new <= conv_threshold) {
      abline(c, m) 
      converged = T
      return(paste("Optimal intercept:", c, "Optimal slope:", m))
    }
    iterations = iterations + 1
    if(iterations > max_iter) { 
      abline(c, m) 
      converged = T
      return(paste("Optimal intercept:", c, "Optimal slope:", m))
    }
  }
}


gradientDesc(disp, mpg, 0.0000293, 0.001, 32, 2500000)





# Temario
# Regresioni Multivariada
plot(women)
women
regresion(women$height, women$weight,ny=139)
plot(y=women$height, x = women$weight, ylab = "Height", xlab = "Weight", )








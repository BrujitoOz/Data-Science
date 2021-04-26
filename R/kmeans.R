set.seed(2020)
x=rnorm(10, mean = rep(c(2:5),each=5), sd = 0.5)
y=rnorm(10, mean = rep(c(1,2,3,4),each=5), sd = 0.3)      
plot(x,y, col="red",pch=8, cex = 1)        
text(x,y,labels = 1:20)
df = data.frame(x,y)

#como estan agrupados los datos

distancias = dist(df)
cluster = hclust(distancias)
plot(cluster)


########################################################################

##obtener los "k" puntos iniciales
k = 3
#forma 1
obtenerKpuntosAleatorios<-function(df, k){
  x1=sample(min(df$x):max(df$x),size = k)
  y1=sample(min(df$y):max(df$y),size = k)
  return (data.frame(x1,y1))  
}
obtenerKpuntosAleatorios(df,k)
#forma 2
obtenerKpuntos<-function(df, k){
  ids<-sample(x = 1:NROW(df),k)
  return (df[ids,])
}
puntos<-obtenerKpuntos(df,k)
class(puntos)

#############################################################
#calculo de las distancias eucldianas
euclidiana<-function(pA,pB) {
  return (sqrt((pA$x-pB$x)^2+(pA$y-pB$y)^2))
}
calcularDistancias<-function(df,puntos){
  dtemp<-df
  for(i in 1:NROW(puntos))
    dtemp[,i+NCOL(df)]<-euclidiana(df,puntos[i,])
  return (dtemp) 
}
calcularDistancias(df,puntos)

calcDistancias<-function(df,puntos){
  m<-matrix(nrow = NROW(df),ncol = NROW(puntos))  
  for(i in 1:NROW(puntos))
    m[,i]<-euclidiana(df,puntos[i,])
  return (m) 
}
m<-calcDistancias(df,puntos)

obtenerGrupos<-function(m){
  matriz<-apply(m,1,min)==m
  grupos<-rep(-1,NROW(m))
  for(i in 1:NCOL(matriz))
    grupos[matriz[,i]]=i
  return (grupos)
}
grupo<-obtenerGrupos(m)

df<-cbind(df,grupo)
############################################################
calcularCentroide<-function(df, puntos){
  # solamente para el grupo1
  px<-c()
  py<-c()
  for(i in 1:NROW(puntos)){
    px<-c(px,mean(df[df$grupo==1,]$x))
    py<-c(py,mean(df[df$grupo==1,]$y))   
  }
  
  puntos<-cbind(px,py)
  return (puntos)
}
puntos<-calcularCentroide(df,puntos)

##TODO invocar a las funciones, y validar convergencia
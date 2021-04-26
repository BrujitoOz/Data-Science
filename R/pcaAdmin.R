datos<-read.csv("sales.csv")
boxplot(datos)#datos anomalos o espureos
summary(datos)
cor(datos)
library(corrplot)
corrplot(cor(datos))
#normalizacion de los datos: estandarizacion(variables- promedio)/desv
datosEsc<-scale(datos)
View(datos)

pca<-prcomp(datosEsc)
summary(pca)
str(pca)#estructura
pca[[1]]#desviaciones
pca[[2]]#rotaciones
pca[[5]]#individuos


componentes<-cbind(pca[[2]][,1], pca[[2]][,2],pca[[2]][,3],pca[[2]][,4])
individuos<-pca[[5]][,c(1:4)]
individuos

install.packages("ade4")#graficar los ejes de rotacion
library(ade4)
x11()
#analisis cluster del componente c1 y c2
s.corcircle(componentes[,c(1,2)])

x11()
#analisis cluster del componente c1 y c3
s.corcircle(componentes[,c(1,3)])

#cuales son los registros que indican  el grado de participacion
x11()
s.label(individuos[,c(1,2)],label = row.names(datos))

datos$Milk
#analisis cluster del componente c1 y c3
x11()
s.corcircle(componentes[,c(1,3)])
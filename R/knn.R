x<-sample(30:60,50,replace = TRUE)
y<-sample(60:100,50,replace = TRUE)

df<-data.frame(x,y)
plot(df)
###Etiquetar (categorizar)
etiquetar<-function(df){
  categorias<-c()
  for(i in 1:NROW(df)){
    if(df$x[i]>=30& df$x[i]<40)
      categorias<-c(categorias,'A') 
    else if(df$x[i]>=40& df$x[i]<50)
      categorias<-c(categorias,'B')
    else categorias<-c(categorias,'C')
  }
  df<-cbind(df,categorias)  
  return (df)
}
df=etiquetar(df)

#######Visualizando el df
library(ggplot2)
ggplot(data = df,aes(x=df$x,y=df$y,color=df$categorias))+
  geom_point()+xlab("X")+ylab("Y")+ggtitle("Clasificador KNN")
#datos para entrenamiento
ids=sample(1:nrow(df),0.85*nrow(df))
dfEnt<-df[ids,]
nrow(dfEnt)
dfTest<-df[-ids,]
nrow(dfTest)
ggplot(data = dfTest ,aes(x=x,y=y,color=categorias))+geom_point()+xlab("X")+ylab("Y")+ggtitle("Clasificador KNN")

dFTemp=df
knn<-function(dFTemp,newX,newY,k, method){
  if(method==1){
    d<-(abs(newX-dFTemp$x)+abs(newY-dFTemp$y))    
  }else{
    d<-sqrt((newX-dFTemp$x)^2+(newY-dFTemp$y)^2)  
  }
  dFTemp<-cbind(dFTemp,d)
  dFTemp  
  vOrden<-sort(dFTemp$d)
  vecinos<-dFTemp[dFTemp$d %in% vOrden[1:k],3]
  return (vecinos[1:k] )
}
# df,x, y, k, metodo
v<-knn(df,40,80,5,2)
v



porc<-function(vector,value){
  return (sum(as.integer(vector==value)))
}
a<-porc(v,"A")
b<-porc(v,"B")
c<-porc(v,"C")
total<-(a+b+c)
a*100/total
b*100/total
c*100/total
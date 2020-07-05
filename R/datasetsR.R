# importar el dataset csv 
dataset = read.csv('Data.csv')

# trata con los nan
dataset$Age = ifelse(is.na(dataset$Age),
                     ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE)),
                     dataset$Age)

dataset$Salary = ifelse(is.na(dataset$Salary), 
                        ave(dataset$Salary, FUN = function(x) mean(x, na.rm=TRUE))
                        ,dataset$Salary)

# codificar las variables categoricas
dataset$Country = factor(dataset$Country, 
                         levels = c("France", "Spain", "Germany"),
                         labels = c(1, 2, 3))

dataset$Purchased = factor(dataset$Purchased,
                           levels = c("No", "Yes"),
                           labels = c(0, 1))


# dividir los datos entre conjunto para entrenamiento, y de testeo

# install.packages("caTools") instalar esta libreria solo necesario una vez
library(caTools)

# Al contrario de python, el argumento indica que porcentaje se usa para entrenar en vez de testear
set.seed(123)
MySplit = sample.split(dataset$Purchased, SplitRatio = 0.8)
# Al imprimir el vector MySplit, todos los true son lo que se usaran para entrenar,  lo false para testing

MyTraining_set = subset(dataset, MySplit==TRUE)
MyTesting_set = subset(dataset, MySplit==FALSE)


# Escalado de valores
MyTraining_set[,2:3] = scale(MyTraining_set[,2:3])
MyTesting_set[,2:3] = scale(MyTesting_set[,2:3])


# Ejecutar
print(dataset)
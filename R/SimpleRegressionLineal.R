# Regresion Lineal Simple

# Importar dataset
dataset = read.csv("Salary_Data.csv")
# SplitRatio se refiere al tamanio de conjunto de entrenamiento
# install.packages("caTools")
library(caTools)
set.seed(123)
split = sample.split(dataset$Salary, SplitRatio = 2/3)
training_set = subset(dataset, split == TRUE) # True son los asignados para entrenar
test_set = subset(dataset, split == FALSE)


# LM LinearMode
MyRegression = lm(formula = Salary ~ YearsExperience, data = training_set) # calcula el Salary(dependiente) en Relacion a YearsExperience(independiente)

# Predecir resultados en conjunto de test
y_pred = predict(MyRegression, newdata = test_set)

# Visualizacion de los resultados en conjunto de entrenamiento
# install.packages("ggplot2")
library(ggplot2)
ggplot() + 
  geom_point(aes(x = training_set$YearsExperience, y = training_set$Salary),
             colour = "red") +
  geom_line(aes(x = training_set$YearsExperience, 
                y = predict(MyRegression, newdata = training_set)),
            colour = "blue") +
  ggtitle("Sueldo vs Anios de Experiencia(Conjunto de entrenamiento)") +
  xlab("Anios de Experiencia") +
  ylab("Sueldo $")


# Visualizacion de los resultados en conjunto de testting
ggplot() + 
  geom_point(aes(x = test_set$YearsExperience, y = test_set$Salary),
             colour = "red") +
  geom_line(aes(x = training_set$YearsExperience, 
                y = predict(MyRegression, newdata = training_set)),
            colour = "blue") +
  ggtitle("Sueldo vs Anios de Experiencia(Conjunto de test)") +
  xlab("Anios de Experiencia") +
  ylab("Sueldo $")

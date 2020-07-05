# Tipos de variables: categoricas -> nominales(hombre, mujer,rojo,verde) 
#                                 -> ordinales(pequeño,mediana,grande, notas, A, B, C)
#                     numericas -> discretas(1,2,3 empleados 568 personas)
#                               -> continuas pueden ser decimales edad, altura
# Regresiones:
# Lineal: Regresion lineal Simple(solo una variable independiente)    Regresion Lineal multiple
# Logistica: Regresion logistica simple(intentar predecir con una sola variable independiente)  Regresion logistica Multiple

# Regresion lineal Simple: y = b0 + b1 * x1 
# sueldo = b0 + b1 + experiencia, donde y = sueldo, x = exp
# la y seria la variable dependiente a predecir, y el x1 la variable independiente 
# La regresion lineal seria la mejor recta que se acerque mas a los puntos


# metodo de los minimos cuadrados: el metodo que usamos para hallar la recta 



# importar librerias
#import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importar el dataset
dataset = pd.read_csv("Salary_Data.csv")
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

# Dvividir el conjunto de datasets en training y testing
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=1/3, random_state=0)

# Cuando la regresion lineal es simple no se necesita reescalar

# Crear modelos de regresion lineal simple
from sklearn.linear_model import LinearRegression
MyRegression = LinearRegression()
MyRegression.fit(x_train, y_train)

# Predecir el conjunto de test
y_pred = MyRegression.predict(x_test)

# Visualizar los resultados de entrenamiento
plt.scatter(x_train, y_train, color = "red")
plt.plot(x_train, MyRegression.predict(x_train), color = "blue")
plt.title("Sueldo vs Anios de Experiencia (Conjunto de Entrenamiento)")
plt.xlabel("Anios de Experiencia")
plt.ylabel("Sueldo en $")
plt.show()

# Visualizar los resultados de test
plt.scatter(x_test, y_test, color = "red")
plt.plot(x_train, MyRegression.predict(x_train), color = "blue") # la recta de regresion lineal es unica
plt.title("Sueldo vs Anios de Experiencia (Conjunto de Entrenamiento)")
plt.xlabel("Anios de Experiencia")
plt.ylabel("Sueldo en $")
plt.show()


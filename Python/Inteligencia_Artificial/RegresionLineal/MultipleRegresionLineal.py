# y -> variable dependiente por ejemplo nota de un alumno
# y = b0 + b1 * x1 + b2*x2 + ... + bn * xn 
# b0 -> la constante(la nota que suele sacar el estudiante cuando las variables independientes son igual a 0)
# las variables independientes(x1,x2...) podrian ser horas de estudio, esfuerzo, etc
# b|,b2 son otras constantes que van juntoa las variables independientes

# Restricciones de la Regresion Lineal
# Linealidad, Homocedasticidad, Normalidad multivariable, independencia de los errores, ausencia de multicolinealidad

# El dataset contiene ganancia vs r&d spend, adminis, marketing, y el estado 
# convertiremos el estado en variables categoricas, new york = 1, california = 0
# Que es un p-valor? es un termino en estadistica que ayuda a determinar si una hipotesis es correcta o no, si por ejemplo el p-value esta debajo de 0.05 un valor predeterminado, la hipotesis se considera nula

# Como construir un modelo: 
# 1.- Exhaustivo(all-in): ingresar todas las variables por conocimiento a prior, necesidad del cliente, o como preparacion previa para Eliminacion hacia atras 
# 2.- Eliminacion hacia atras:
    # 1.- Seleccionar el nivel de significacion para permanecer en el modelo SL=0.05
    # 2.- Se calcula el modelo con todas las posibles variables predictorias
    # 3.- Considera la variable predictora con el p-value mas grande, si P > SL entonces vamos al punto 4, sino vamos al 5
    # 4.- Se elimina la variable predictora
    # 5.- Se ajusta desde sero el modelo sin dicha variable
# 3.- Seleccion hacia adelante
    # 1.- Elegimos un nivel de significacion para el modelos SL = 0.05
    # 2.- Ajustamos el modelo de regresion lineal simple y ~ xn, y elegimos el de menor p-value
    # 3.- Conservamos esta variable y ajustamos todos los posibles modelos hasta el momento
    # 4.- Consideramos la variable predictora con el menor p-value, si P < SL vamos al paso 3, sino a 5
    # 5.- Nos quedamos con el modelo anterior
    
# 4.- Eliminacion bidireccional
    # 1.- seleccionar un nivel de significacion para entrar y salir
    # 2.- Llevar a cabo Seleccion hacia adelante con las nuevas varialbes P < SL-Enter
    # 3.- "" Eliminacion hacia atras con P < SL-Stay
    # 4.- Repetir 2 ultimos pasos hasta que no haya variables que puedan entrar o salir
# 5.- Comparacion de scores
    # 1.- Seleccionar un criterio de bondad de ajuste e.j cireterio de Akaike
    # 2.- Construir todos los posibles modelos de regresion 2^n-1 combinaciones en total
    # 3.- Seleccionar el modelo con mejor cirterio
import pandas as pd
import numpy as np
dataset = pd.read_csv("50_Startups.csv")
# x toma las varialbes independientes: gasto de recursos, administracion, marketing y estado, Y tiene el beneficio
x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values

# Codificar datos categoricos
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
MyLabelEnconder_X = LabelEncoder() # Clase que convierte a numeros
x[:, 3] = MyLabelEnconder_X.fit_transform(x[:, 3]) # ajusta y reemplaza por numeros unicos para cada estado
from sklearn.compose import ColumnTransformer
ct = ColumnTransformer([('one_hot_encoder', OneHotEncoder(categories='auto'), [3])] , remainder = 'passthrough')
x = np.array( ct.fit_transform(x), dtype=np.int )

# Evitar la trampa de las variables dummy, nos conviene eliminar una columna
x = x[:, 1:] 

# Dividir entre conjuntos trainy test
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test =  train_test_split(x,y,test_size=1/5, random_state = 0)

# Ajustar el modelos de regresion lineal al multiple
from sklearn.linear_model import LinearRegression
MyRegression = LinearRegression()
MyRegression.fit(x_train, y_train)

# Prediccion de los resultados 
y_pred = MyRegression.predict(x_test)

# Construir el modelo optimo de ALM utilizando eliminacion hacia atras
# import statsmodels.formula.api as sm
x = np.append(arr = np.ones((50,1)).astype(int), values = x, axis = 1)









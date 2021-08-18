import pandas as pd #es una liberia para dataframe va de la mano con numpy
import numpy as np #brinda ayuda con vectores y matrices, liberia matematica
import matplotlib.pyplot as mptl #generacion de graficos a partir de matrices o arrays

#escanear un csv con pandas
mydataset = pd.read_csv("Data.csv") 
#iloc nos ayuda a indicar que porcion agarrar
x = mydataset.iloc[:, :-1].values #todas las filas, todas las columnas menos la ultima
y = mydataset.iloc[:, 3].values #todas las filas, solo columna indice 3
print(mydataset)



#tratamiento de los nan
from sklearn.impute import SimpleImputer # es una liberia para machine learning, trabaja junto con numpy y scipy
MyImputer = SimpleImputer(missing_values=np.nan, strategy='mean', verbose=0) #creamos el imputer para sacar media
MyImputer = MyImputer.fit(x[:, 1:3]) # ajustamos el imputer a la matriz x, columna 1 a 2
x[:, 1:3] = MyImputer.transform(x[:, 1:3]) # reempĺazamos
#x[:, 1:3] = MyImputer.fit_transform(x[:, 1:3]) forma de hacerlo en un solo paso



#tratamiento de datos categoricos como el Yes No 
#LabelEncoder convierte valores como nombres de paises a numeros clave para cada palabra
#OneHotEncoder representa las variables categoricas en vectores binarios
#StandardScale reescala valores de distinta escala como salarios y edades
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer

labelencoder_x = LabelEncoder() #creamos el objeto
x[:, 0] = labelencoder_x.fit_transform(x[:, 0])#le indicamos que transforme la columna con nombres de paises

# para que los numeros no sean ordinales usamos onehot encoder para tener variables dummy

# ColumnTransformer recibe nombre, transform, y columna
ct = ColumnTransformer( [('one_hot_encoder', OneHotEncoder(categories='auto'), [0])], remainder='passthrough')
# remainder dice que pase de las demas columnas

# usamos np.array para ajustar y darle los nuevos valores a la matriz x, de paso indicar que el array sea float
x = np.array(ct.fit_transform(x), dtype=np.float)

# Al usar el LabelEncoder se convertira en 0 y 1
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)



# Dividir el dataset en conjunto de entrenamiento y de testing
from sklearn.model_selection import train_test_split
#usamos un train para entrenar al algoritmo, y un test para verificar si funciona
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0) # le damos x a dividir, y lo que queremos predecir, el y, el test_size indica que porcentaje de test usaremos lo comun es usar 20%, 30 a lo mucho, el random state es apra que nos de el mismo resultado



# trabajando con escalado de variables
MyEscalador_x = StandardScaler() # creamos nuestro escalador
x_train = MyEscalador_x.fit_transform(x_train)
x_test = MyEscalador_x.transform(x_test) # damos solo transform para trabajar con el mismo fit, o sea el mismo escalado



# Ahora veremos la simple linear regression, multiple regresion lineal, polinomial, suppor vector for regression svr, decision tree classification, y random forest classification
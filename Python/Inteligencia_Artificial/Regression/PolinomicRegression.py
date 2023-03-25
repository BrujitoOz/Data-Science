#%% Lectura
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
dataset = pd.read_csv("../Datasets/Position_Salaries.csv")
x = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values
#%% Ajustar regresion lineal
from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm.fit(x, y)
#%% Correlacion
import seaborn as sns
sns.pairplot(dataset)
print(dataset.corr())
#%% Ajustar regresion polinomica
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(9)
x_poly = poly_reg.fit_transform(x)
lm2 = LinearRegression()
lm2.fit(x_poly, y)
y_pred = lm2.predict(x_poly)
print(pd.DataFrame({'Prediction':np.around(y_pred,2), 'True': y}))
#%% Metricas
from sklearn.metrics import mean_squared_error, mean_absolute_error
print("MSE:", mean_squared_error(y, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y, y_pred)))
print("MSA:", mean_absolute_error(y, y_pred))
#%% Regresion polinomica
xlabel = "Posicion del empleado"
ylabel = "Sueldo (en $)"
plt.scatter(x, y, color = "red")
plt.plot(x, lm2.predict(x_poly), color = "blue")
plt.title("Modelo de regresion polinomica")
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.show()
# Regresion polinomica suavizada
x_grid = np.arange(min(x), 10.1, 0.1)
x_grid = x_grid.reshape(len(x_grid) ,1)
plt.scatter(x, y, color = "red")
plt.plot(x_grid, lm2.predict(  poly_reg.fit_transform(x_grid) ), color = "blue")
plt.title("Modelo de regresion polinomica suavizada")
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.show()
# %%

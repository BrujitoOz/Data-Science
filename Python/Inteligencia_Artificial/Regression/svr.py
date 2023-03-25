#%% Lectura
import numpy as np
import pandas as pd
dataset = pd.read_csv("../Datasets/Position_Salaries.csv")
x = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values
#%% Reescalar
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
sc_y = StandardScaler()
x = sc_x.fit_transform(x)
y = sc_y.fit_transform(y.reshape(-1,1))
#%% Ajustar
from sklearn.svm import SVR
regression = SVR(kernel = "rbf")
regression.fit(x,y)
#%% Prediccion
y_pred = sc_y.inverse_transform(regression.predict((x)))
#%% Metricas
from sklearn.metrics import mean_squared_error, mean_absolute_error
print("MSE:", mean_squared_error(sc_y.inverse_transform(y), y_pred))
print("RMSE:", np.sqrt(mean_squared_error(sc_y.inverse_transform(y), y_pred)))
print("MSA:", mean_absolute_error(sc_y.inverse_transform(y), y_pred))
#%% Grafico
import matplotlib.pyplot as plt
x_grid = np.arange(min(x),max(x),0.1)
x_grid = x_grid.reshape(len(x_grid), 1)
plt.scatter(sc_x.inverse_transform(x), sc_y.inverse_transform(y), color = "red")
plt.plot(sc_x.inverse_transform(x_grid), sc_y.inverse_transform(regression.predict(x_grid)), color = "blue")
plt.title("Modelo de regresion SVR")
plt.xlabel("Posicion del empleado")
plt.ylabel("Sueldo (en $)")
plt.show()
# %%

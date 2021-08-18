#%% Lectura
import numpy as np
import pandas as pd
dataset = pd.read_csv("Position_Salaries.csv")
x = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values
#%% Entrenamiento
from sklearn.ensemble import RandomForestRegressor
regression = RandomForestRegressor(n_estimators = 10, random_state = 0)
regression.fit(x,y)
#%% Prediccion
y_pred = regression.predict(x)
#%% Metricas
from sklearn.metrics import mean_squared_error, mean_absolute_error
print("MSE:", mean_squared_error(y, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y, y_pred)))
print("MSA:", mean_absolute_error(y, y_pred))
#%% Grafico
import matplotlib.pyplot as plt
x_grid = np.arange(min(x), 10.1, 0.001)
x_grid = x_grid.reshape(len(x_grid), 1)
plt.scatter(x,y, color="red")
plt.plot(x_grid, regression.predict(x_grid))
plt.show()
#%%
pred = regression.predict([[6.5]])
pred
# %%

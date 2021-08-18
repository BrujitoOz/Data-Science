#%% Lectura
import pandas as pd
import numpy as np
dataset = pd.read_csv("50_Startups.csv")
x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values
#%% Correlacion
import seaborn as sns
sns.pairplot(dataset)
print(dataset.corr())
#%% Visualizacion
cmap = sns.diverging_palette(0, 255, as_cmap=True)
sns.heatmap(dataset.corr(), cmap=cmap)
#%% Tratar datos categoricos
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
MyLabelEnconder_X = LabelEncoder()
x[:, 3] = MyLabelEnconder_X.fit_transform(x[:, 3])
from sklearn.compose import ColumnTransformer
ct = ColumnTransformer([('one_hot_encoder', OneHotEncoder(categories='auto'), [3])] , remainder = 'passthrough')
x = np.array(ct.fit_transform(x), dtype=np.int)
x = x[:, 1:] 
#%% Calculating VIF for each feature
from statsmodels.stats.outliers_influence import variance_inflation_factor
def calc_vif(X, features):
    X = pd.DataFrame(X)
    vif = pd.DataFrame()
    vif["variables"] = features
    vif["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
    return vif
features = ['Florida','New York','R&D Spend', 'Administration', 'Marketing Spend']
calc_vif(x, features)
#%% Dividir entre conjuntos train y test
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test =  train_test_split(x, y, test_size=1/5, random_state = 0)
#%% Entrenamiento
from sklearn.linear_model import LinearRegression
MyRegression = LinearRegression()
MyRegression.fit(x_train, y_train)
#%% Interpretar coeficientes
print(MyRegression.intercept_)
print(MyRegression.coef_)
#%% Prediccion de los resultados
y_pred = MyRegression.predict(x_test)
print(pd.DataFrame({'Prediction':np.around(y_pred,2), 'True':y_test}))
#%% Metricas
from sklearn.metrics import mean_squared_error, mean_absolute_error
print("MSE:", mean_squared_error(y_test, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))
print("MSA:", mean_absolute_error(y_test, y_pred))
#%% Construir el modelo optimo usando Backward Elimination
import statsmodels.api as sm
x = np.append(arr = np.ones((50,1)).astype(int), values = x, axis = 1)
#%% backwardElimination
SL = 0.05
x_opt = x[:, [0,1,2,3,4,5]]
regressionOLS = sm.OLS(y, x.tolist()).fit()
regressionOLS.summary()
#%% Tomando en cuenta P value
def backwardEliminationPvalue(x, sl):    
    n = len(x[0])    
    for i in range(0, n):        
        regressionOLS = sm.OLS(y, x.tolist()).fit()        
        maxval = max(regressionOLS.pvalues).astype(float)        
        if maxval > sl:            
            for j in range(0, n - i):                
                if (regressionOLS.pvalues[j].astype(float) == maxval):                    
                    x = np.delete(x, j, 1)    
    regressionOLS.summary()
    return x      
SL = 0.05
X_opt = x[:, [0, 1, 2, 3, 4, 5]]
X_Modeled = backwardEliminationPvalue(X_opt, SL)
#%% Opción alternativa tomando en cuenta P value y R cuadrado ajustado
def backwardEliminationPAndR2(x, SL):    
    n = len(x[0])    
    temp = np.zeros((50,6)).astype(int)    
    for i in range(0, n):        
        regressor_OLS = sm.OLS(y, x.tolist()).fit()        
        maxVar = max(regressor_OLS.pvalues).astype(float)        
        adjR_before = regressor_OLS.rsquared_adj.astype(float)        
        if maxVar > SL:            
            for j in range(0, n - i):                
                if (regressor_OLS.pvalues[j].astype(float) == maxVar):                    
                    temp[:,j] = x[:, j]                    
                    x = np.delete(x, j, 1)                    
                    tmp_regressor = sm.OLS(y, x.tolist()).fit()                    
                    adjR_after = tmp_regressor.rsquared_adj.astype(float)                    
                    if (adjR_before >= adjR_after):                        
                        x_rollback = np.hstack((x, temp[:,[0,j]]))                        
                        x_rollback = np.delete(x_rollback, j, 1)     
                        print (regressor_OLS.summary())                        
                        return x_rollback                    
                    else:                        
                        continue    
    regressor_OLS.summary()    
    return x
SL = 0.05
X_opt = x[:, [0, 1, 2, 3, 4, 5]]
X_Modeled = backwardEliminationPAndR2(X_opt, SL)
# %%

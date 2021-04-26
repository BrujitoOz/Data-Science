# librerias
import numpy as np
import pandas as pd

# importar dataset 
ds = pd.read_csv("Data.csv")
x = ds.iloc[:,]
x = ds.iloc[:,:].values
print(x)
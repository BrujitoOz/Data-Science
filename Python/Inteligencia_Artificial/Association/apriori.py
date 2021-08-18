#%% Dataset
import numpy as np
import pandas as pd
dataset = pd.read_csv("Market_Basket_Optimisation.csv", header=None)
#%% Lista de listas
transaction = []
for i in range(0, 7501):
    transaction.append([str(dataset.values[i, j]) for j in range(0,20)])
#%% Entrenar
#from apyori import apriori
# min lenght longitud minima de la regla de asociasion, support presencia minima de un item como umbral, 
rules = apriori(transaction, min_support = 3*7/7500, min_confidence = 0.2,min_lift = 3, min_length = 2)
# %%

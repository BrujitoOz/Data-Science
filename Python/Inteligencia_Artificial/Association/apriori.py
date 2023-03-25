#%% Dataset
import pandas as pd
dataset = pd.read_csv("../Datasets/Market_Basket_Optimisation.csv", header=None)
#%% Lista de listas
transaction = []
for i in range(0, 7501):
    transaction.append([str(dataset.values[i, j]) for j in range(0,20)])
#%% Entrenar
import apyori
# support presencia minima de un item como umbral(productos comprados al menos 3 veces por dia en una semana)
# minima confianza (comenzar con 0.8 e ir reduciendolo hasta llegar a encontrar reglas de asociacion)
# min lift(probabilidad de que se compre el artículo “B” cuando se compra el artículo “A”)
# min lenght longitud minima de la regla de asociasion(analizar al menos 2 productos),
rules = apyori.apriori(transaction, min_support = 3*7/7500, min_confidence = 0.2,
                       min_lift = 3, min_length = 2)

# %%
results = list(rules)

# %%

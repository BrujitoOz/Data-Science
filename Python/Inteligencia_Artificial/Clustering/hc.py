#%% Dataset
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
dataset = pd.read_csv("../Datasets/Mall_Customers.csv")
x = dataset.iloc[:, [3,4]].values
#%% dendrograma: busca la distancia mas grande para elegir el n de cluster
import scipy.cluster.hierarchy as sch
def dendrograma(metodo, xl, yl):
    sch.dendrogram(sch.linkage(x, method = metodo))
    plt.title("dendrograma")
    plt.xlabel(xl)
    plt.ylabel(yl)
    plt.show()
dendrograma("ward", "clientes", "distancia euclidea")
#%% Entrenamiento
from sklearn.cluster import AgglomerativeClustering
hc = AgglomerativeClustering(n_clusters = 5, affinity="euclidean", linkage="ward")
y_hc = hc.fit_predict(x)
print(y_hc)

def MyClustering(n, kmeans, y, titulo, xlabel, ylabel):
    color = ["red", "blue", "green", "cyan", "magenta", "yellow"]
    for i in range(n):
        plt.scatter(x[y == i, 0], x[y == i, 1], s = 100, c = color[i], label = "Cluester {}".format(i+1))
    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.show()
MyClustering(5, None, y_hc, "Cluster de clientes", "Ingresos anuales (en miles de $)","Puntuacion de gasos (1-100)")
# %%

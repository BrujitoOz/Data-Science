#%% Dataset
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
dataset = pd.read_csv("Mall_Customers.csv")
x = dataset.iloc[:,[3,4]].values
#%% Metodo del codo
from sklearn.cluster import KMeans
def metodoDelCodo(x):
    wcss = []
    for i in range(1, 11):
        kmeans = KMeans(n_clusters = i, init = "k-means++", max_iter = 300, n_init = 10, random_state = 0)
        kmeans.fit(x)
        wcss.append(kmeans.inertia_)
    plt.plot(range(1,11), wcss)
    plt.title("Metodo del codo")
    plt.xlabel("Numero de clusters")
    plt.ylabel("WCSS(k)")
    plt.show()

#%% Entrenamiento
kmeans = KMeans(n_clusters = 5, init = "k-means++", max_iter = 300, n_init = 10, random_state = 0)
y_kmeans = kmeans.fit_predict(x)
print(y_kmeans)
def KMeansClustering(n, kmeans, y_kmeans, titulo, xlabel, ylabel):
    color = ["red", "blue", "green", "cyan", "magenta", "yellow"]
    names = ["F2P With $","Standard","Whale With $","Whale W/O $", "F2P W/O $"]
    for i in range(n):
        plt.scatter(x[y_kmeans == i, 0], x[y_kmeans == i, 1], s = 100, c = color[i], label = names[i])
    #plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:,1], s=300, c="black", label= "Baricentros")
    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.show()
KMeansClustering(5, kmeans, y_kmeans, "Cluster", "annual revenue","Score (1-100)")
# %%

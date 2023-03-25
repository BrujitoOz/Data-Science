#%% Leer dataset
import numpy as np
import pandas as pd
dataset = pd.read_csv("../Datasets/Social_Network_ads.csv")
x = dataset.iloc[:, [2,3]].values
y = dataset.iloc[:, 4].values
#%% Dividir
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=0)
#%% Escalado
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test)
#%% Entrenamiento
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators=10, criterion="entropy", random_state=0)
classifier.fit(x_train, y_train)
#%% Prediccion
y_pred = classifier.predict(x_test)
print(y_pred)
print(y_test)
#%% Matriz
from sklearn .metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
def MatrizdeConfusion(cm):
    print(pd.DataFrame({' ':['No', 'Si'],'No':cm[0],'Si':cm[1]}))
    aciertos = 0
    desaceritos = 0
    for i in range(len(cm[0])):
        aciertos += cm[i][i]
    desaceritos = sum(sum(cm))
    desaceritos -= abs(aciertos) 
    print("Cantidad aciertos:",aciertos)
    print("Cantidad desaciertos:",desaceritos)
MatrizdeConfusion(cm)

#%% Visualizacion
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
def graphic(x, y, titulo):
    X_set, y_set = x, y
    X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
                        np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
    plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
                alpha = 0.75, cmap = ListedColormap(('red', 'green')))
    plt.xlim(X1.min(), X1.max())
    plt.ylim(X2.min(), X2.max())
    for i, j in enumerate(np.unique(y_set)):
        plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                    c = ['red', 'green'][i], label = j)
    plt.title(titulo)
    plt.xlabel('Edad')
    plt.ylabel('Sueldo Estimado')
    plt.legend()
    plt.show()
graphic(x_train, y_train, "Clasificador Arboles de desicion (Conjunto de Entrenamiento)")
graphic(x_test, y_test, "Clasificador Arboles de desicion (Conjunto de Test)")

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets


def minimonodo(data, t, pesos, n_rows, ncols):
    BMU = (0, 0) # posicion de la neurona, la mas cercana a la neurona
    distanciaminima = 1.0e20
    for i in range(n_rows):
        for j in range(ncols):
            de = euc_dist(pesos[i][j], data[t]) 
            if de < distanciaminima:
                distanciaminima = de
                BMU = (i, j)
    return BMU

def euc_dist(v1, v2):
    return np.linalg.norm(v1-v2)
# rango de espacio de agrupacion
def man_dist(r1,c1,r2,c2):
    return (np.abs(r1-r2) + np.abs(c1-c2))

# entrenamiento
def som():
    atributos = 4
    rows = 30
    cols = 30
    rangomax = rows + cols
    factoraprendizaje = 0.3
    iteraciones = 100
    dataentrenamiento = datasets.load_iris()
    salida = dataentrenamiento.target
    dataentrenamiento = dataentrenamiento.data[:, :4]
    # inicializar pesos
    pesos = np.random.randn(rows, cols, atributos)
    for s in range(iteraciones):
        alfa = 1.0 - ((s * 1.0) / iteraciones)
        rangoactual = (int) (alfa*rangomax)
        alfaactual = alfa* factoraprendizaje
        t = np.random.randint(len(dataentrenamiento))
        (bmu_row, bmu_col) = minimonodo(dataentrenamiento, t, pesos, rows, cols)
        for i in range(rows):
            for j in range(cols):
                if man_dist(bmu_row, bmu_col, i, j) < rangoactual:
                    pesos[i][j] = pesos[i][j] + alfaactual * (dataentrenamiento[t] - pesos[i][j])

    for t in range(len(dataentrenamiento)):
        (bmu_row, bmu_col) = minimonodo(dataentrenamiento, t, pesos, rows, cols)
        print(t, " ", bmu_row, " ", bmu_col, " ", pesos[bmu_row][bmu_col])
    # visualizacion
    print("visualizacion")
    mapa = np.empty(shape=(rows, cols), dtype=np.int64)
    for i in range(rows):
        for j in range(cols):
            mapa[i][j] = -1
    for t in range(len(dataentrenamiento)):
        (bmu_row, bmu_col) = minimonodo(dataentrenamiento, t, pesos, rows, cols)
        mapa[bmu_row][bmu_col] = salida[t]
    plt.imshow(mapa)
    plt.colorbar()
    plt.show()
som()


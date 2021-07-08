import numpy as np

# entrenamiento con hopfield
def hopfield(entradas):
    n = len(entradas[0])
    w = np.zeros([n, n])
    for patron in entradas:
        matrizentrada = np.matrix(patron)
        sum_w = matrizentrada.T * matrizentrada
        np.fill_diagonal(sum_w, 0)
        w += sum_w
    return w
# funcion de activacion
def f(matriz):
    matriz[matriz >= 0] = 1
    matriz[matriz < 0] = -1
    return matriz
# entradas
entradas = [[1, 1, -1, -1], [-1, -1, 1, 1]]
U = hopfield(entradas)
print(U)
# evaluacion
while True:
    resp1 = np.dot(U, np.matrix([1, -1, -1, -1]).T) 
    print(f(resp1))
    resp2 = np.dot(U, resp1) 
    print(f(resp2))
    if (np.all( resp1 == resp2)):
        print("Hay convergencia")
        break

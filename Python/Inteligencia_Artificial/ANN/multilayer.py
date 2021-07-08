import numpy as np
def sigmoid(x):
  return 1/(1 + np.exp(-x))
def sigmoid_derivative(x):
  return x*(1-x)
def calcf(h_pesos, entradas):
    return sigmoid(h_pesos[0] * entradas[0] + h_pesos[1] * entradas[1])
entradas = [
  [0,0],
  [0,1],
  [1,0],
  [1,1]
]
output = [
  [0],
  [1],
  [1],
  [0]
]
h_pesos = [
    [0.100, -0.700],
    [0.500, 0.300]
]
o_pesos = [
    [0.200, 0.400]
]
h_bias = [
    [0.5, 0.5]
]
o_bias = 0.5
epocas = 0
lr = 0.25
i = 0

while True:
    for j in range(len(entradas)):
        # Propagacion hacia adelante
        # Capa oculta con funcion sigmoidal
        n1 = calcf(h_pesos[0], entradas[j])
        n2 = calcf(h_pesos[1], entradas[j])
        # uso de umbral para capa oculta
        n1 += h_bias[0][0]
        n2 += h_bias[0][1]
        aux = [n1, n2]
        # Capa de salida con funcion sigmoidal
        y = calcf(o_pesos[0], aux)
        # uso de umbral para capa salida
        y += o_bias

        # Propagacion hacia atras
        # Calculo delta de capa salida
        error = abs(output[j] - y)
        delta_o = sigmoid_derivative(y) * (error)
        # Nuevos pesos capa salida
        o_pesos[0][0] += lr * n1 * delta_o
        o_pesos[0][1] += lr * n2 * delta_o
        o_bias += lr * delta_o
        # Nuevos pesos capa oculta
        # Neurona 1
        delta_y1 = sigmoid_derivative(n1) * o_pesos[0][0] * delta_o 
        h_pesos[0][0] += lr * entradas[0][0] * delta_y1
        h_pesos[0][1] += lr * entradas[0][1] * delta_y1
        h_bias[0][0] = lr * delta_y1
        # Neurona 2
        delta_y2 = sigmoid_derivative(n2) * o_pesos[0][1] * delta_o
        h_pesos[1][0] += lr * entradas[0][0] * delta_y2 
        h_pesos[1][1] += lr * entradas[0][1] * delta_y2
        h_bias[0][1] += lr * delta_y2
        i+=1
    epocas+=1
    if epocas == 2000:
        break
print(h_pesos)
print(o_pesos)
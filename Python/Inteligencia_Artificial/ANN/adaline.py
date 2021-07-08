
def f(pesos, entrada, dx):
    # calc
    y = pesos[0] * entrada[0] + pesos[1] * entrada[1] + pesos[2] * entrada[2]
    error = abs(dx - y)
    return y, error
def act(pesos, entrada, a, error):
    pesos[0] += a * error * entrada[0]
    pesos[1] += a * error * entrada[1]
    pesos[2] += a * error * entrada[2]
    return pesos

pesos = [3.4, 2.01, 1.00]
a = 0.3
entradas = [
    [0, 0, 1],
    [0, 1, 0],
    [0, 1, 1],
    [1, 0, 0],
    [1, 0, 1],
    [1, 1, 0],
    [1, 1, 1]
]
dx = [1, 2, 3, 4, 5, 6, 7]

iteraciones = 6
for i in range(iteraciones):
    y, error = f(pesos, entradas[i], dx[i])
    pesos = act(pesos, entradas[i], a, error)
    print("----------")
    print("iteracion:",i)
    print("y:",y)
    print("error:",error)
    print("pesos:",pesos)
    print("----------")


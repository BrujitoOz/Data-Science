def f(pesos, entrada, umbral):
    # calc
    y = pesos[0] * entrada[0] + pesos[1] * entrada[1] + umbral
    # escalonar
    if y > 0:
        return 1
    elif y <= 0:
        return -1
def act(pesos, entrada, umbral, dx):
    pesos[0] += dx * entrada[0]
    pesos[1] += dx * entrada[1]
    umbral += dx
    return pesos, umbral

pesos = [1, 0.5]
umbral = 0
entradas = [
    [-2, -1],
    [-1, -1.5],
    [2, -2],
    [-2, 1],
    [1.5, 0.5],
    [1, 1]
]
dx = [-1, -1, -1, 1, 1, 1]


termino = False
while True:
    termino = True
    # inicia epoca
    for i in range(len(entradas)):
        y = f(pesos, entradas[i], umbral)
        # checkar si esta mal clasificado y actualizar
        if y != dx[i]:
            termino = False
            while y != dx[i]:
                # actualizar
                pesos, umbral = act(pesos, entradas[i], umbral, dx[i])
                y = f(pesos, entradas[i], umbral)
    # termina epoca
    if termino:
        break

print(pesos)
print(umbral)
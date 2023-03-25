# funcion de activacion
def f(pesos, entrada, umbral):
    # calc
    y = pesos[0] * entrada[0] + pesos[1] * entrada[1] + umbral
    # escalonar
    if y > 0:
        return 1
    elif y <= 0:
        return -1
# actualizar pesos
def actpesos(pesos, dx, entrada):
    pesos[0] += dx * entrada[0]
    pesos[1] += dx * entrada[1]
    return pesos
def actumbral(umbral, dx):
    umbral += dx
    return umbral

# main
neuronas = 2
entradas = [
    [-1, -1],
    [1, -1],
    [-1, 1],
    [1, 1]
]
dx = [-1, -1, -1, 1]
pesos = [1, 1]
umbral = 0.5
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
                pesos = actpesos(pesos, dx[i], entradas[i])
                umbral = actumbral(umbral, dx[i])
                y = f(pesos, entradas[i], umbral)
    # termina epoca
    if termino:
        break

print(pesos)
print(umbral)
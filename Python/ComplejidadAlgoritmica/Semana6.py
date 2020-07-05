#%%
# 1: Codear un algoritmo con complejida nlogn o menos, que busque si existe una suma superior a un numero dado
def SubSumAlg(arr, n, s) :
    if (s == 0) :
        return True
    if (n == 0 and s != 0) :
        return False
    if (arr[n-1] > s) :
        return SubSumAlg(arr, n-1, s)
    return SubSumAlg(arr, n-1, s) or SubSumAlg(arr, n-1, s-arr[n-1])
arr = [8, 7, 3, 1, 9, 5]
print(SubSumAlg(arr, len(arr), 10))
# %%
# 2: hallar la suma maxima de los elementos de dos arreglos usando un algoritmo con complejidad 2T(2/b) + c  
def Max(arr, i, f):
    if i == f:
        return arr[i]
    med = (i + f) // 2
    izq = Max(arr, i, med)
    der = Max(arr, med+1, f)
    if izq > der:
        return izq
    else:
        return der
A = [8,7,3,1,13,5]
B = [7,5,2,11,1]
arr = list(set(i for i in (A + B)))
print(Max(arr, 0, len(arr)-1))
#%%
# 3: 
# inciso a: armar lista de adyacencia
G = [
    [(2, 1)],#A 0
    [(0, 1), (8, 4)],#B 1
    [(1, 2), (8, 1)],#C 2
    [(1, 5), (4, 3)],#D 3
    [(2, 7)],#E 4
    [(3, 6), (4, 10), (6, 2), (7, 2)],#F 5
    [(1, 21)],#G 6
    [(3, 11), (5, 3)],#H 7
    []
]
#%%
# inciso b: buscar ruta corta e indicar la couta minima para llegar al destino
t = 8
n = len(G)
path = [None for i in range(n)]
visited = [False for i in range(n)]
def dfs(G, u):
    global t
    if u == t and not visited[u]:
        visited[u] = True
        return
    if not visited[u]:
        visited[u] = True
    for v,w in G[u]:
        if not visited[v]:
            path[v] = u
            dfs(G, v)
    return path
print(dfs(G, 7))
#%%
# inciso c: buscar el camino más corto
from heapq import heappush, heappop
import math
def ucs(G, start, end):
    n = len(G)
    visited = [False for i in range(n)]
    weight = [math.inf for i in range(n)]
    path = [None for i in range(n)]
    queue = []
    heappush(queue, (0, start))
    weight[start] = 0
    while len(queue) > 0:
        print("queue", queue)
        PesoPadre, NodoPadre = heappop(queue)
        if NodoPadre == end:
            break
        if visited[NodoPadre]:
            continue
        visited[NodoPadre] = True
        for NodoHijo, PesoHijo in G[NodoPadre]:
            if not visited[NodoHijo]:
                NuevoPeso = PesoPadre + PesoHijo
                if NuevoPeso < weight[NodoHijo]:
                    weight[NodoHijo] = NuevoPeso
                    path[NodoHijo] = NodoPadre
                    heappush(queue, (NuevoPeso, NodoHijo))
    return path, weight

path, weights = ucs(G, 7, 8)
names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
last = 8
while last != None:
    print(names[last], last)
    last = path[last]
# inciso d: indicar complejidad de los algoritmos usados
"""
El algoritmo del inciso c tiene un Big O de V + E, vértices y aristas sumadas
El algoritmo del inciso d tiene complejidad O(b^(d+1)) c costo de trayectoria más corta y e menor de
los costos
"""
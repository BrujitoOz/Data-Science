# Repaso 
cont = 0
def recursivo(n):
  global cont
  cont +=1
  if n==1 or n==0:
   return 1
  return recursivo(n-1)+2*n
n=8
for i in range(n):
  print(recursivo(i))
print("Iteraciones, ", cont)

print("---Con programación Dinámica")

cont2 = 0
def pdinamica(n):  
  cache = [0 for i in range(n)]
  cache[0]=1
  cache[1]=1
  global cont2
  cont2+=1
  for i in range(2,n):
    cache[i]=cache[i-1]+2*i
    cont2+=1
  return cache

print("Con programación dinamica")
print(pdinamica(n))
print(cont2)


coruna, vigo, valladolid, bilbao,oviedo, madrid,badajoz, zaaragoza,albacete,jaen,murcia, sevilla, granada = 0,1,2,3,4,5,6,7,8,9,10,11,12
G = [
  [(vigo,171),(valladolid,455)],#coruna
  [(coruna,171),(valladolid,356)],#vigo
  [(coruna,455),(vigo,171),(bilbao,280),(madrid,193)],#valladolid
  [(oviedo,304),(valladolid,280),(madrid,395),(zaaragoza,324)],#bilbao
  [(bilbao,304)],#oviedo
  [(badajoz,403), (valladolid,193),(bilbao,395),(zaaragoza,325),(albacete,251),(jaen,335)],#madrid
  [(madrid,403)],#badajoz
  [(bilbao,324),(madrid,395)],#zaaragoza
  [(murcia,150),(madrid,251)],#albacete
  [(sevilla,242),(granada,99),(madrid,251)],#jaen
  [(albacete,150),(granada,278)],#murcia
  [(jaen,242),(granada,256)],#sevilla
  [(jaen,99),(murcia,278),(sevilla,256)]   #sevilla
]
from math import inf
import heapq
def Dijkstra(G, s):
  n = len(G)
  visited = [False for _ in range(n)]
  weights = [inf for _ in range(n)]
  path = [None for _ in range(n)]
  queue = []
  weights[s] = 0
  heapq.heappush(queue, (0, s))
  while len(queue) > 0:
    g, u = heapq.heappop(queue)
    visited[u] = True
    for v, w in G[u]:
      if not visited[v]:
        f = g + w
        if f < weights[v]:
          #print(f,weights[v])
          weights[v] = f
          path[v] = u
          heapq.heappush(queue, (f, v))
  return path, weights

p, w = Dijkstra(G, bilbao)
L =['coruna', 'vigo', 'valladolid', 'bilbao','oviedo', 'madrid','badajoz', 'zaaragoza','albacete','jaen','murcia', 'sevilla', 'granada']
def printpath(path,dist, f, F):
  if f!=None:
    printpath(path,dist, path[f],F)
    print(L[f], end =' ')
  else:
    print('W=%2.0f:' %(dist[F]), end =' ')
for n in range(len(G)):
    printpath(p, w, n, n)
    print()

# PC2:
# 1.
# Modificar  el  algoritmo  recursivo  representado  en  el programa, ee implementar  
# el  algoritmo de  programación  dinámica respectivoque imprima  
# los C primeros términos de la secuencia:
def funcionRecursiva(n,s):
    if n < 1:
        return s
    else:
        return funcionRecursiva(n-1, s + n)
def funcionRecursivaDP(n,s):
    cache = [-1 for _ in range(n+1)]
    def f(n, s):
        if n < 1:
            return s
        if cache[n] != -1:
            return cache[n]
        else:
            cache[n] = f(n-1, s + n)
            return cache[n]
    f(n, s)
    return cache[n]
n = 5
print(funcionRecursiva(n,0))
print(funcionRecursivaDP(n,0))
# 2. 
# i: es la posición del término T, el primer término está en la posición 1
# 1, 5, 15, 34, 65, 111
# Escribir  el  programa  recursivo que imprima la secuencia de los C primeros términos.
# Imprimir la cantidad de iteraciones realizadas para hallar el valor de un término cualquiera.
# Escribir el programa dinámico que imprima la secuencia de los C primeros términos.
# Imprimir la suma de la sucesión de términos.
cont = 0
def suce(n):
    global cont
    cont+=1
    if n == 1:
        return 1
    if n == 2:
        return 5
    else:
        return 2 * suce(n-1) - suce(n-2) + 3 * (n-1)
# 1, 5, 15, 34, 65, 111
c = 5 # i = 5 -> 65
print("1. Recursivo:", suce(c))
print("2. Cant iteraciones:", cont)
# 3.
# Una  empresa  de  reparto  planifica  las  rutas  de  su  flota  de  camiones  
# entre distintas ciudades. Tenemos un grafo que representa el mapa de carreteras, 
# siendo T[v, w]el tiempo que se tarda entre los puntos vy w. 
# En general, nos interesa pasar por elcamino que  nos  permita  ocupar el menor tiempo  posible.  
# Pero últimamente  suceden imprevistos, como atascos, accidentes o de cortes en lascarreteras. 
# Diseñar un algoritmo que encuentre el camino de menor tiempo entre dos nodos dados del grafoe imprimir la ruta y el tiempo. 
# Aplicarlo al grafo de la figura para encontrar el camino mínimo entre 1 y 7.

G = [
    [(1,2), (3, 4)], # 0
    [(2, 8), (3, 3)], # 1
    [(4, 3)], # 2
    [(2, 2), (4, 1), (5,3), (6,8)], # 3
    [(6, 10)], # 4
    [(6, 6)], # 5
    [],
]
from math import inf
import heapq
def Dijkstra(G, s):
  n = len(G)
  visited = [False for _ in range(n)]
  weights = [inf for _ in range(n)]
  path = [None for _ in range(n)]
  queue = []
  weights[s] = 0
  heapq.heappush(queue, (0, s))
  while len(queue) > 0:
    g, u = heapq.heappop(queue)
    visited[u] = True
    for v, w in G[u]:
      if not visited[v]:
        f = g + w
        if f < weights[v]:
          #print(f,weights[v])
          weights[v] = f
          path[v] = u
          heapq.heappush(queue, (f, v))
  return path, weights

p, w = Dijkstra(G, 0)
L =['1','2','3','4','5','6', '7']
def printpath(path,dist, f, F):
  if f!=None:
    printpath(path,dist, path[f],F)
    print(L[f], end =' ')
  else:
    print('W=%2.0f:' %(dist[F]), end =' ')
printpath(p, w, 6, 6)




# 4.
# La tabla muestra la capacidad máxima diaria de buses entre varias ciudades (en cientos de personas). 
# Dibuje una red para mostrar las capacidades de las rutas desde Londres a Newcastle se sabe que 
# se está celebrando un festival en Newcastle. Encuentre el  número  máximo  de  personas  que  
# pueden  viajar  en  autobús  desde  Londres  para  el festival.
# Grafique un diagrama de la red
# Implemente un algoritmo que encuentre un flujo máximo para la red 
# Grafique el grafo Flujo etiquetando cada arista con su flujo real.
# Investigue  qué  sucede  cuando  hay  una  huelga  en  una  de  las  estaciones  de autobuses de Liverpool, justifique su respuesta.
G = [
    [(bir, 40), (lds, 20)], # lon
    [(man, 10), (lds, 15), (lpl, 12)], # bir
    [(lds, 12), (new, 15)], # man
    [(new, 30)], # lds
    [(man, 7), (new, 8)], #lpl
    []
]
from math import inf
def bfs(graph, start, end, path):
  size = len(graph)
  visited = [False for _ in range(size)]
  queue = []
  queue.append(start)
  visited[start] = True
  while len(queue) > 0:
    idx = queue.pop(0)
    for jdx, val in enumerate(graph[idx]):
      if not visited[jdx] and val > 0:
        visited[jdx] = True
        queue.append(jdx)
        path[jdx] = idx
  return visited[end]

def FordFulkerson(G,start, end):
  n = len(G)
  max_flow = 0
  path = [None for i in range(n)]
  dgraph = [[0 for x in range(n)] for x in range(n)]
  rgraph = [[0 for x in range(n)] for x in range(n)]
  for u, node in enumerate(G):
    for v,w in node:
      dgraph[u][v] = w

  while bfs(dgraph, start, end, path):
    min_flow = inf
    temp = end 
    while temp!=start: 
      min_flow= min(min_flow,dgraph[path[temp]][temp])      
      temp = path[temp]
    #print("min_flow ",min_flow)
    max_flow += min_flow
    temp = end
    while temp != start:
      dgraph[path[temp]][temp] -= min_flow
      rgraph[path[temp]][temp] += min_flow
      temp = path[temp]
  return max_flow, rgraph

lon, bir, man, lds, lpl, new = 0,1,2,3,4,5
m, f = FordFulkerson(G,0,5) 
print("2. Flujo maximo:", m) 
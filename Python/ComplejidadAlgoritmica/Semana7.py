# Semana 7: Orden topologico, Componentes fuertemente conexos
# Orden topologico
def orden_topo(Graph):
  cantidad = len(Graph)
  visitados = [False for _ in range(cantidad)]
  pila = []
  # implementar DFS
  def dfs(nodo):
    if visitados[nodo]:
      return
    visitados[nodo] = True
    for vecinos in Graph[nodo]:
      if visitados[vecinos] == True:
        continue
      dfs(vecinos)
    pila.append(nodo)
  dfs(2) # empieza
  return list(reversed(pila))

def run():
  Graph = [
    [1,2],
    [2,3],
    [4],
    [4],
    []
  ]
  Grafo = [
    [1,2],  #0
    [3,4], #1 
    [5,6], #2
    [7],   #3
    [8,9], #4
    [9],   #5
    [11],  #6
    [10], #7
    [10], #8
    [11], #9
    [12], #10
    [12], #11
    [] #12
  ]
  ruta = orden_topo(Grafo)
  print(ruta)
  ruta2 = orden_topo(Graph)
  print(ruta2)
run()

# Componentes fuertemente conexos
import heapq as hp
def Kosaraju(Grafo):
  cantidad = len(Grafo)
  GrafoInvertido = [[] for _ in range(cantidad)]
  for u in range(cantidad):
    for v in Grafo[u]:
      GrafoInvertido[v].append(u)
  cola = []
  visitados = [False] * cantidad
  indice = [0]
  # primerDFS
  def dfs1(nodo):
    if not visitados[nodo]:
      visitados[nodo] = True
      for v in GrafoInvertido[nodo]:
        dfs1(v)
      indice[0] += 1
      hp.heappush(cola, (cantidad - indice[0], nodo))
  for u in range(cantidad):
    dfs1(u)
  cfcResultado = []
  visitados = [False] * cantidad
  def dfs2(nodo, SubGrafo):
    if not visitados[nodo]:
      visitados[nodo] = True
      for v in Grafo[nodo]:
        dfs2(v, SubGrafo)
      SubGrafo.append(nodo)
  while len(cola) > 0:
    _,nodo = hp.heappop(cola)
    if not visitados[nodo]:
      SubGrafo = []
      dfs2(nodo, SubGrafo)
      cfcResultado.append(SubGrafo)
  return cfcResultado
G = [
  [6],
  [4],
  [8],
  [0],
  [7],
  [2,7],
  [3,8],
  [1],
  [5]
]
print(Kosaraju(G))
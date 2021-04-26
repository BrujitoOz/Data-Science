class Edge(object):
    def __init__(self, cityB, distance):
        self.cityB = cityB
        self.distance = distance


class Node(object):  # tipo objeto
    def __init__(self, city):
        self.city = city
        self.hs = h[city]
        self.fs = 0
        self.parent_node = None

    def isGoal(self):
        return goalNodo == self.city


class NodeList(list):
    def find(self, city):
        l = [t for t in self if t.city == city]
        return l[0] if l != [] else None

    def remove(self, node):
        del self[self.index(node)]


def addEdge(cityA, cityB, distance):
    graph[cities[cityA]].append(Edge(cityB, distance))
    graph[cities[cityB]].append(Edge(cityA, distance))


cities = {'Arad': 0, 'Bucharest': 1, 'Craiova': 2, 'Dobreta': 3, 'Eforie': 4, 'Fagaras': 5, 'Giurgiu': 6, 'Hirsova': 7,
          'Iasi': 8, 'Lugoj': 9,
          'Mehadia': 10, 'Neamt': 11, 'Oradea': 12, 'Pitesti': 13, 'Rimnicu Vilcea': 14, 'Sibiu': 15, 'Timisoara': 16,
          'Urziceni': 17, 'Vaslui': 18, 'Zerind': 19}
graph = [[], [], [], [], [], [], [], [], [],
         [], [], [], [], [], [], [], [], [], [], []]

h = {'Arad': 366, 'Bucharest': 0, 'Craiova': 160, 'Dobreta': 242, 'Eforie': 161, 'Fagaras': 178, 'Giurgiu': 77,
     'Hirsova': 151, 'Iasi': 226, 'Lugoj': 244,
     'Mehadia': 241, 'Neamt': 234, 'Oradea': 380, 'Pitesti': 98, 'Rimnicu Vilcea': 193, 'Sibiu': 253, 'Timisoara': 329,
     'Urziceni': 80, 'Vaslui': 199, 'Zerind': 374}

addEdge('Arad', 'Zerind', 75)
addEdge('Zerind', 'Oradea', 71)
addEdge('Oradea', 'Sibiu', 151)
addEdge('Arad', 'Sibiu', 140)
addEdge('Arad', 'Timisoara', 118)
addEdge('Timisoara', 'Lugoj', 111)
addEdge('Lugoj', 'Mehadia', 70)
addEdge('Mehadia', 'Dobreta', 75)
addEdge('Dobreta', 'Craiova', 120)
addEdge('Sibiu', 'Fagaras', 99)
addEdge('Sibiu', 'Rimnicu Vilcea', 80)
addEdge('Rimnicu Vilcea', 'Pitesti', 97)
addEdge('Rimnicu Vilcea', 'Craiova', 146)
addEdge('Craiova', 'Pitesti', 138)
addEdge('Fagaras', 'Bucharest', 211)
addEdge('Pitesti', 'Bucharest', 101)
addEdge('Bucharest', 'Giurgiu', 90)
addEdge('Bucharest', 'Urziceni', 85)
addEdge('Urziceni', 'Hirsova', 98)
addEdge('Hirsova', 'Eforie', 86)
addEdge('Urziceni', 'Vaslui', 142)
addEdge('Vaslui', 'Iasi', 92)
addEdge('Iasi', 'Neamt', 87)


startNodo = 'Arad'
goalNodo = 'Bucharest'

openList = NodeList()
closeList = NodeList()
startNode = Node(startNodo)
startNode.fs = startNode.hs
openList.append(startNode)
endNode = None

while True:
    if openList == []:
        print("There is no route until reaching a goal.")
        exit(1)
    n = min(openList, key=lambda x: x.fs)
    openList.remove(n)
    closeList.append(n)
    if n.isGoal():
        endNode = n
        break
    for v in graph[cities[n.city]]:
        cityB = v.cityB
        m = openList.find(cityB)
        dist = v.distance
        if m:
            if m.fs > m.hs:
                m.fs = m.hs
                m.parent_node = n
        else:
            m = closeList.find(cityB)
            if m:
                if m.fs > m.hs:
                    m.fs = m.hs
                    m.parent_node = n
                    openList.append(m)
                    closeList.remove(m)
            else:
                m = Node(cityB)
                m.fs = m.hs
                m.parent_node = n
                openList.append(m)
n = endNode
sol = []
while True:
    sol.append(n.city)
    if n.parent_node == None:
        break
    n = n.parent_node
sol.reverse()
print(list(sol))

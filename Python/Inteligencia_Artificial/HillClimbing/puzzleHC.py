import time, copy, random
import numpy as np
from collections import deque

class BoardState(): #Estado del tablero
	def __init__(self, paquete, parent, action, f:int, h:int, zeroPos):
		self.matrix = np.matrix(np.array(paquete[0]).reshape(paquete[1][0], paquete[1][1]))
		self.parent = parent #Apunta al estado anterior
		self.action = action #Dirección que toma el slide vacio
		self.f = f #Número de estados que se puede retroceder
		self.h = h #Herística basada en la cantidad de posiciones incorrectas
		self.zeroPos = zeroPos
		self.children = []

	def locateZero(self):
		self.zeroPos = [i[0] for i in np.where(self.matrix==0)]

	def sameState(self, other_state):
		if self.matrix == other_state.matrix:
			return True
		return False 


class BoardStructure(): #Representación logica del tablero
	def __init__(self, witdh, height):
		self.width = witdh
		self.height = height
		self.id = self.identifyWithKeys()
		self.adyacentes = self.linkBetweenSlides()

	#Retorna una matriz con claves (IDs) 
	#   las cuales pueden ser accesadas usando [fila][columna]
	def identifyWithKeys(self):   
		key = []
		num = 0
		for _i in range(self.width):
			aux = [None]*self.width
			for j in range(self.height):
				aux[j] = num
				num +=1
			key.append(aux)
		return key

	def addEdge(self, ady, pos1:tuple, pos2:tuple):
		i1, j1, i2, j2 = pos1[0], pos1[1], pos2[0], pos2[1]
		ady[self.id[i1][j1]].append(pos2)
		ady[self.id[i2][j2]].append(pos1)

	#Para cada posición establece cuales son sus adyacentes
	def linkBetweenSlides(self):
		# ady = [[]]*(self.width*self.height)
		ady = [[] for e in range(self.width*self.height)]
		#Vertical
		for i in range(self.width-1):
			for j in range(self.height):
				self.addEdge(ady, (i, j), (i + 1, j))
		#Horizontal
		for i in range(self.width):
			for j in range(self.height-1):
				self.addEdge(ady, (i, j), (i, j + 1))
		return ady

#Board es enrealidad el conjunto de todos los estados de table, SpaceTime
class SpaceTime():
	def __init__(self, init_pack, goal_pack):
		#self.board = board
		self.init_state = BoardState(init_pack, None, None, 0, None, None) #Aqui tdv no se le asigna un valor de heuristica
		self.goal_state = BoardState(goal_pack, None, None, None, 0, None)
		self.board = BoardStructure(self.init_state.matrix.shape[0], self.init_state.matrix.shape[1])
		self.goal_vec = self.convertToVecPos(goal_pack[0], goal_pack[1][0], goal_pack[1][1])

	def convertToVecPos(self, vec, fila, col):
		aux = {}
		ctn = 0
		for i in range(fila):
			for j in range(col):
				aux[vec[ctn]] = (i, j)
				ctn += 1
		ls = [0]*(fila*col)
		for k, v in aux.items():
			ls[k] = v
		return ls

	def not_matching_pos(self, currentMatrix, goal_pos):
		#Goal aqui no es una matriz, es un vector de tuplas
		#filas, columas
		costos = 0
		fila, columna = currentMatrix.shape
		for i in range(fila):
			for j in range(columna):
				valor = currentMatrix[i,j]
				if valor==0:
					continue
				ig, jg = goal_pos[valor]
				if (ig, jg)!=(i,j): 
					costos+=1
		return costos

	def solve(self, limit):
		def inside(ls, state):
			for another_state in ls:
				if np.array_equal(state.matrix, another_state.matrix):
					return True
			return False

		def genNewState(state, i, j): #verifica que funciones
			aux = copy.copy(state)
			aux.matrix = state.matrix.copy()
			i0, j0 = aux.zeroPos
			aux.matrix[i, j], aux.matrix[i0, j0] =\
				aux.matrix[i0, j0], aux.matrix[i, j] 
			aux.zeroPos = [i, j]
			aux.h = self.not_matching_pos(aux.matrix, self.goal_vec)
			aux.f = aux.h
			return aux

		def generateNextState(state):
			possible_movements = []
			zero_i, zero_j = state.zeroPos
			zero_id = self.board.id[zero_i][zero_j]
			#genera hasta 4 nuevos estados posibles usando las coordenadas
			for i, j in self.board.adyacentes[zero_id]:
				new_state = copy.copy(genNewState(state, i, j))
				new_state.parent = state
				#if not is_adopted(state):
				if state.parent == None:
					possible_movements.append(new_state)
				else:
					if not np.array_equal(new_state.matrix, state.parent.matrix): #CONFIO Q RESISTE
						possible_movements.append(new_state)
			state.children.extend(possible_movements)
		
		self.init_state.locateZero()
		self.init_state.f = self.not_matching_pos(self.init_state.matrix, self.goal_vec)	

		depth = 0
		children_list = []
		start_time = time.time()

		if (self.init_state.f==0):
			self.goal_state.parent = self.init_state.parent
			return
		else:
			generateNextState(self.init_state)
			for child in self.init_state.children:
				children_list.append(child)
			exist_state = children_list
			current_state = self.init_state
			
			while len(children_list)!=0:
				end_time = time.time()
				if (end_time-start_time) > limit:
					print("No se alcanzo una solucion en", limit , "segundos")
					exit(1)
				
				children_list = sorted(children_list, key=lambda x: x.f)
				if current_state.f > children_list[0].f:
					if (len(children_list) == 1) or children_list[0].f < children_list[1].f:
						current_state=children_list[0]
					else:
						aux = []
						for child in children_list:
							if child == children_list[0]:
								aux.append(child)
						index = random.randint(0,len(aux)-1)
						current_state= aux[index]
				else: 
					index = random.randint(0,len(children_list)-1)
					current_state = children_list[index]

				# If this child is not the solution, gentrate children of this child	
				if (current_state.f==0):
					self.goal_state.parent = current_state.parent
					break
				else:
					generateNextState(current_state)
					if len(current_state.children) != 0:
						for child in current_state.children:
							flag = 0
							for node_state in exist_state:
								if np.array_equal(\
									node_state.matrix,child.matrix):
									flag = 1
							if flag == 0:
								child.f = self.not_matching_pos(child.matrix, self.goal_vec)
								depth +=1
								children_list.append(child)
								exist_state.append(child)


if __name__ == '__main__':
	test1 =	([1, 2, 0, 4, 5, 3, 7, 8, 6], (3, 3))
	test2 =	([0, 1, 3, 4, 2, 5, 7, 8, 6], (3, 3))
	test3 = ([8, 1, 3, 2, 0, 5, 4, 7, 6], (3, 3)) #Excede 10s
	test4 =	([1, 2, 3, 5, 6, 4, 7, 8, 0], (3, 3)) #Excede 10s
	test5 = ([6, 0, 2, 1, 8, 3, 7, 4, 5], (3, 3)) #Excede 10s
	test6 = ([0, 3, 5, 1, 2, 6, 8, 4, 7], (3, 3)) #Excede 10s

	goal0 = ([1, 2, 3, 4, 5, 6, 7, 8, 0], (3, 3))

	test7 = ([2, 8, 3, 
	          1, 6, 4,
			  7, 0, 5], (3, 3))
	goal1 = ([1, 2, 3, 
	          8, 0, 4, 
			  7, 6, 5], (3, 3))

	b = SpaceTime(test7, goal1)


	b.solve(10)

	path = []
	estado = b.goal_state
	count = 0
	while (estado != None):
		path.append((count, estado.matrix))
		estado = estado.parent
		count +=1
	path.reverse()
	[print("\n\n", 'Step', len(path)-i, "\n", e) for i, e in path]
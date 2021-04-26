import copy
import random
import numpy as np


class Queen:
    def __init__(self, id = 0, x = 0, y = 0):
        self.id = id
        self.x = x
        self.y = y

def CountCheck(Queen_List, Actual_Queen):
	Checks = 0
	for i in Queen_List:
		#Ignores the actual Queen
		if i == Actual_Queen:
			continue
		#Check for horizontal and vertical checks
		if i.x == Actual_Queen.x or i.y == Actual_Queen.y:
			Checks += 1
			continue
		#Check for diagonal checks
		if abs(i.x - Actual_Queen.x) == abs(i.y - Actual_Queen.y):
			Checks += 1
			continue
	return Checks

def HillClimbing(Queen_List):
    #Creates a copy of the Queens array
    aux_List = copy.deepcopy(Queen_List)
    #Shuffles the list
    random.shuffle(aux_List)
    #Checks counter
    Total_Checks = 0
    #Assigns a position to every queen on the array
    for queen in aux_List:
        #Starts as a hight value so the first try will be the better
        aux_Checks = 9999
        #Saves the index of the current best position
        aux_Best = 0
        #Tries every posible position
        for i in range(8):
            queen.x = i
            if CountCheck(aux_List, queen) < aux_Checks:
                #Changes the checks amount if its lower
                aux_Checks = CountCheck(aux_List, queen)
                #Updates the best position
                aux_Best = i
            if i == 7:
                #On the last iteration assigns the best position founded
                queen.x = aux_Best
        #Updates the total amount of checks
        Total_Checks += aux_Checks
    return aux_List, Total_Checks

def SolveProblem(Queen_List):
    #Creates a copy of the Queens array
    aux_List = copy.deepcopy(Queen_List)
    #Checks counter
    Total_Checks = 0
    while True:
        #Executes the algorithm untill it finds a solution
        aux = HillClimbing(aux_List)
        #Stops once theres no checks
        if aux[1] == 0:
            return aux[0]
#=============================================================


#Board size declared
board_size = 8
#Board creation
Board = np.zeros(shape = (board_size, board_size)).astype(int)
Boardi = Board.copy()

#List of queens created
Queen_List = []
#List filled with one queen per Y level
for i in range(Board[0].size):
	aux = Queen(i, 0, i)
	Queen_List.append(aux)

for i in Queen_List:
    Boardi[i.x, i.y] = 1
    print("(",i.x,",",i.y,")")

print("=================")
Queen_List = SolveProblem(Queen_List)

for i in Queen_List:
    print("(",i.x,",",i.y,")")
    Board[i.x,i.y] = 1

print("=========TABLERO INICIAL=================")
print(Boardi)
print("=========TABLERO FINAL=================")
print(Board)
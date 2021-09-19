#%% Libreria
from ortools.sat.python import cp_model
n = 10
#%% Crear CSP
model = cp_model.CpModel()
# Variables y dominios
grilla = []
for i in range(n):
    fila = []
    for j in range(n):
        fila += [model.NewIntVar(1, n,'x'+str(i)+str(j))]
    grilla += [fila]
print(grilla)
# Restricciones
for i in range(n):
    # Toda fila tiene valores distintos
    model.AddAllDifferent(grilla[i])
    # Toda columna tiene valores distintos
    model.AddAllDifferent([x[i] for x in grilla])
# Cages
model.Add(grilla[0][0] - grilla[1][0] == 3)
model.Add(grilla[0][1] + grilla[1][1] == 7)
model.Add(grilla[0][2] + grilla[0][3] + grilla[0][4] + grilla[1][3] + grilla[1][4] == 38)
model.Add(grilla[0][5] + grilla[0][6] + grilla[1][5] + grilla[1][6] == 23)
model.Add(grilla[0][7] + grilla[1][7] + grilla[2][7] + grilla[1][8] == 23)
model.Add(grilla[0][8] + grilla[0][9] == 9)
model.Add(grilla[1][2] + grilla[2][2] + grilla[2][3] == 8)
model.Add(grilla[1][9] + grilla[2][8] + grilla[2][9] == 16)
model.Add(grilla[2][0] - grilla[2][1] == 1)
model.Add(grilla[2][4] == 5)
model.Add(grilla[2][5] + grilla[3][5] + grilla[3][6] == 11)
model.Add(grilla[2][6] == 6)
model.Add(grilla[3][0] == 8)
model.Add(grilla[3][1] + grilla[3][2] + grilla[3][3] + grilla[3][4] == 25)
model.Add(grilla[3][7] + grilla[3][8] + grilla[4][7] == 21)
model.Add(grilla[3][9] == 4)
model.Add(grilla[4][0] == 3)
model.Add(grilla[4][1] + grilla[5][0] + grilla[5][1]  == 14)
model.Add(grilla[4][2] == 2)
model.Add(grilla[4][3] + grilla[4][4] + grilla[4][5] + grilla[5][5] == 28)
model.Add(grilla[4][6] == 5)
model.Add(grilla[4][8] + grilla[5][8] == 6)
model.Add(grilla[4][9] - grilla[5][9] == 7)
model.Add( grilla[6][2] - grilla[5][2] == 2)
model.Add(grilla[5][3] + grilla[5][4] + grilla[6][3] == 19)
model.Add(grilla[5][6] - grilla[6][6] == 7)
model.Add(grilla[5][7] == 3)
model.Add(grilla[6][0] + grilla[7][0] + grilla[8][0] == 20)
model.Add(grilla[6][1] == 6)
model.Add(grilla[6][4] == 3)
model.Add(grilla[6][5] + grilla[7][5] + grilla[7][6] + grilla[8][5]  == 19)
model.Add(grilla[6][7] + grilla[6][8] == 11)
model.Add(grilla[6][9] + grilla[7][9] == 14)
model.Add(grilla[7][1] + grilla[7][2] + grilla[8][1] + grilla[8][2] == 19)
model.Add(grilla[7][3] == 2)
model.Add(grilla[8][3] + grilla[8][4] + grilla[7][4] == 16)
model.Add(grilla[7][7] + grilla[7][8] + grilla[8][6]  + grilla[8][7] == 24)
model.Add(grilla[8][9] - grilla[8][8] == 7)
model.Add(grilla[9][0] == 1)
model.Add(grilla[9][1] - grilla[9][2] == 2)
model.Add(grilla[9][3] == 3)
model.Add(grilla[9][4] == 6)
model.Add(grilla[9][5] + grilla[9][6] + grilla[9][7] + grilla[9][8] + grilla[9][9] == 27)
# Solucion
solver = cp_model.CpSolver()
status = solver.Solve(model)
if status == 4:
    for i in range(n):
        for j in range(n):
            if solver.Value(grilla[i][j]) != 10:
                print("0"+str(solver.Value(grilla[i][j])), end = " ")
            else:
                print(str(solver.Value(grilla[i][j])), end = " ")
        print()
else:
    print("No existe solucion")
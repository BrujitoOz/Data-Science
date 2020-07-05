from numpy import linalg, random, dot, diag, transpose
from numbers import Integral
from math import sqrt
def ValidaOrdenDeLaMatriz():
 while True:
   N = int(input("Ingresa el orden N de la matriz: "))
   if N >= 4 and N <= 10:
     break
 return N
def check_random_state(seed):
 if seed is None or seed is random:
   return random.mtrand._rand
 if isinstance(seed, Integral):
   return random.RandomState(seed)
 if isinstance(seed, random.RandomState):
   return seed
 raise ValueError('%r cannot be used to seed a numpy.random.RandomState'
                    ' instance' % seed)
def make_spd_matrix(n_dim, random_state=None):
 generator = check_random_state(random_state)
 A = generator.rand(n_dim, n_dim)
 U, s, V = linalg.svd(dot(A.T, A))
 X = dot(dot(U, 1.0 + diag(generator.rand(n_dim))), V)
 return X
def GenerarMatrizSimetrica(N):
 matrix = make_spd_matrix(N)
 return matrix
def Cholesky(matrix):
 L = [[0] * len(matrix) for _ in range(len(matrix))]
 N = len(matrix)
 for q in range(N):
   L[q][q] = sqrt(matrix[q][q] - sum(L[q][k]**2 for k in range(q)))
   for p in range(q, N):
     L[p][q] = (matrix[p][q] - sum(L[p][l]*L[q][l] for l in range(q))) / L[q][q]
 return L
def ImprimeMatriz(m):
 for i in range(len(m)):
   for j in range(len(m)):
     print("[",round(m[i][j],2),"]",end=" ")
   print()
def Respuesta(matrix, L):
 print("Matriz Generada:")
 ImprimeMatriz(matrix)
 print("Matriz Triangular inferior:")
 ImprimeMatriz(L)
def Compara(matrix):
 AT = transpose(matrix)
 for i in range(len(matrix)):
   for j in range(len(matrix)):
     if matrix[i][j] != AT[i][j]:
       return False
 return True
def IngresaMatriz(N):
 a = []
 for i in range(N):
   b = []
   for j in range(N):
     print("[",i,"]","[",j,"]: ",end=" ")
     b.append(int(input()))
   a.append(b)
 return a
def DescomposicionDeCholesky():
 N = ValidaOrdenDeLaMatriz()
 matrix = GenerarMatrizSimetrica(N)
 L = Cholesky(matrix)
 Respuesta(matrix, L)
def MatrizDePrueba(matrix):
 Condicion1 = Compara(matrix)
 Condicion2 = all(linalg.eigvals(matrix) > 0)
 if Condicion1 and Condicion2:
   L = Cholesky(matrix)
   Respuesta(matrix, L)
 elif not Condicion1 and not Condicion2:
   print("La matriz ni es simetrica ni es positiva definida")
 elif not Condicion1:
   print("La matriz no es simetrica")
 elif not Condicion2:
   print("La matriz no es positiva definida")

while True:
    print("-----------------------")
    print("Cholesky Decomposition")
    print("1.- Genera Matriz Simetrica Positiva al azar")
    print("2.- Ingresa una Matriz")
    print("3.- Salir")
    print("-----------------------")
    opt = int(input("Elige una opcion: "))
    if opt == 1:
        DescomposicionDeCholesky()
    elif opt == 2:
        N = int(input("Ingresa orden N de la matriz: "))
        mymatrix = IngresaMatriz(N)
        MatrizDePrueba(mymatrix)
    elif opt == 3:
        print("bye!!!")
        break
    else:
     print("No es una opcion habilitada.")
# ejercicio 1 - método de thomas en matriz tridiagonal

from black import err
from sympy import false, true


def ejer1():
  # FUNCTIONS
  # Crear una matriz compuesta de ceros
  def createMatriz(size):
    # Se podría utilizar la librería numpy y evitar esta function
    # L = np.zeros(n,n)
    aux = []
    for i in range(size):
      a = []; 
      for j in range(size):
        if i == j:
          a.append(1)
        else:
          a.append(0)
      aux.append(a);
    return aux;
    
  # calculate values of a matrix lower
  def calculateValuesLower(uniqueMatriz):
    valEcuaciones = []
    for i in range(n):
      sum = uniqueMatriz[i][n]
      for j in range(i):
        sum = sum - uniqueMatriz[i][j] * valEcuaciones[j];
      valEcuaciones.append(sum/uniqueMatriz[i][i]);
    return valEcuaciones;

  # calculate values of a matriz upper
  def calculateValuesUpper(uniqueMatriz):
    valEcuaciones = []
    for i in reversed(range(n)):
      sum = uniqueMatriz[i][n];
      for j in reversed(range(i+1,n)):
        sum = sum - uniqueMatriz[i][j]*valEcuaciones[n-j-1];
      valEcuaciones = [*valEcuaciones, sum/uniqueMatriz[i][i]]
    return valEcuaciones  

  A = [
    [0.5,-2.7,0,0],
    [1,-0.2,-3,0],
    [0,4.9,-7.8,4],
    [0, 0,2.8,-3.4]
  ]
  equationsValues = [
    -5.925,-1.35,4.975,-0.1
  ]
  
  e = 0
  f = 0

  n = len(A); 
  L = createMatriz(n)

  
  for i in range(n-1):
    if i == 0:
      e = A[i+1][i] / A[i][i]
    else:
      e = A[i+1][i] / f
    
    # formar la matriz u
    A[i+1][i] = 0
    
    # insert matrix L
    L[i+1][i] = e

    f = A[i+1][i+1] - e*A[i][i+1]
    
    # insert matrix U
    A[i+1][i+1] = f;          

  print("L")
  for i in L:
    print(i)

  # insertar los values de la equation en L
  for i in range(len(equationsValues)):
    L[i].append(equationsValues[i])
  
  # news values
  equationsValues = calculateValuesLower(L);


  print("U")
  for i in A:
    print(i)

  # insert values in U
  for i in range(len(equationsValues)):
    A[i].append(equationsValues[i])

  # news values
  equationsValues = calculateValuesUpper(A);
  print("VALORES")
  print(equationsValues)

# método de gauss seidel
def gausSeidel():

  # FUNCTIONS
  def diagonalDominante(matrix):
    for j in range(len(matrix)):
      for i in range(j, len(matrix)):
        if abs(matrix[j][j]) < abs(matrix[i][j]):
          aux = matrix[j]
          matrix[j] = matrix[i]
          matrix[i] = aux
    return matrix
  
  def createArrayCeros(l):
    matrixAux = []
    for i in range(l):
      matrixAux.append(0)
    return matrixAux
    
  # VARIABLES
  M = [
    [3,-4,5,-7,19],
    [1,2,-4,5,31],
    [2,-4,5,-1,21],
    [3,-1,7,5,10]
  ];
  # tamaño de la matriz
  n = len(M)
  # error admitido
  ea = 0.01

  # diagonal dominante
  M = diagonalDominante(M)

  values = createArrayCeros(n)
  errores = []
  while(true):
    for i in range(n):
      sum = M[i][n]
      for k in range(n):
        if i != k:
          sum = sum - M[i][k]*values[k]
      aux = values[i]
      values[i] = sum / M[i][i]
      errores.append(abs(1-(aux/values[i])))

    if max(errores) < ea:
      break;
    errores = []  

  # mostrar los resultados  
  for i in range(len(values)):
    print(f"x{i} = {values[i]} - error = {errores[i]}")  
gausSeidel()


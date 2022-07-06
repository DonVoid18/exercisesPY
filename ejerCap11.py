# ejercicio 1 - método de thomas en matriz tridiagonal

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
      print(sum,uniqueMatriz[i][i], sum/uniqueMatriz[i][i])   
    return valEcuaciones;
  # calculate values of a matriz upper
  def calculateValuesUpper(uniqueMatriz):
    print(uniqueMatriz)
    valEcuaciones = []
    for i in reversed(range(n)):
      sum = uniqueMatriz[i][n];
      for j in reversed(range(i+1,n)):
        sum = sum - uniqueMatriz[i][j]*valEcuaciones[n-j-1];
      print(sum, uniqueMatriz[i][i])
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

  L = createMatriz(len(A))
  U = createMatriz(len(A))

  n = len(A); 
  
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
    
  # insertar los values de la equation en L
  for i in range(len(equationsValues)):
    L[i].append(equationsValues[i])
  
  # news values
  equationsValues = calculateValuesLower(L);


  # insert values in U
  for i in range(len(equationsValues)):
    A[i].append(equationsValues[i])
  # news values
  equationsValues = calculateValuesUpper(A);
  print(equationsValues)
ejer1()
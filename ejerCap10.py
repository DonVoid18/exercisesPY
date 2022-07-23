# LIBRERÍAS UTILIZADAS
import numpy as np


# PROBLEMAS DEL CAPÍTULO 10
# ejercicio 1
def ejer1():
#   Utilice las reglas de la multiplicación de matrices para
# demostrar que las ecuaciones (10.7) y (10.8) se obtienen de la
# (10.6).
  m1 = [
    [2,-3,5],
    [6,-1,3],
    [-4,1,-2]
  ]
  # m1 = [
  #   [3,-0.1,-0.2],
  #   [0.1,7,-0.3],
  #   [0.3,-0.2,10]
  # ]

  # sirve para la creación de una matriz que se adecue a L
  def createMatriz(size):
    aux = []
    for i in range(size):
      a = []; 
      for j in range(size):
         a.append(0)
      aux.append(a);
    return aux;
  L = createMatriz(len(m1));

  # 1. calcular la u con el método de gaus
  # 2. rellenar los valores de L a la vez
  # metodo de gaus
  n = len(m1);
  
  for j in range(n):
    for i in range(n):
      if i == j:
        pMatriz = m1[i]
        pivo = m1[i][j]
        # matriz L
        L[i][j] = 1;
      if i>j:
        L[i][j] = m1[i][j]/pivo
        newAList = list(map(lambda x: x*(m1[i][j]/pivo) , pMatriz))
        m1[i] = list(map(lambda x,y: x-y , m1[i],newAList));

  # imprimir la matriz
  print("EL VALOR DE L")
  for i in range(n):
    print(L[i]);
  print("EL VALOR DE U")
  for i in range(n):
    print(m1[i]);
  
  
  
  # el orden de la multiplicación es importante
  # m1 * L != L * m1 
  print("MULTIPLICACIÓN")
  multi = np.dot(L,m1)
  print(multi)

# ejercicio 2
def ejer2():
  # m1 = [
  #   [10,2,-1,27],
  #   [-3,-6,2,-61.5],
  #   [1,1,-5,-21.5]
  # ]
  m1 = [
    [1,2,1,8],
    [-1,3,-2,1],
    [3,4,-7,10]
  ]
  def createMatriz(size):
    aux = []
    for i in range(size):
      a = []; 
      for j in range(size):
         a.append(0)
      aux.append(a);
    return aux;
  
  L = createMatriz(len(m1));

  n = len(m1);
  
  for j in range(n):
    for i in range(n):
      if i == j:
        pMatriz = m1[i]
        pivo = m1[i][j]
        # matriz L
        L[i][j] = 1;
      if i>j:
        L[i][j] = m1[i][j]/pivo
        newAList = list(map(lambda x: x*(m1[i][j]/pivo) , pMatriz))
        m1[i] = list(map(lambda x,y: x-y , m1[i],newAList));

  print("EL VALOR DE U")
  for i in range(n):
    print(m1[i]);

  m1[::-1]
  
  valEcuaciones = []
  for i in reversed(range(n)):
    sum = m1[i][n];
    for j in reversed(range(i+1,n)):
      sum = sum - m1[i][j]*valEcuaciones[n-j-1];
    valEcuaciones = [*valEcuaciones, sum/m1[i][i]]

  # insertar los valores en L
  for i in range(len(valEcuaciones)):
    L[i].append(valEcuaciones[i])
  
  print("EL VALOR DE L")
  for i in range(n):
    print(L[i]);

  valEcuaciones = []
  for i in reversed(range(n)):
    sum = L[i][n];
    for j in reversed(range(i+1,n)):
      sum = sum - L[i][j]*valEcuaciones[n-j-1];
    valEcuaciones = [*valEcuaciones, sum/L[i][i]]
  print("RESULTADO")
  print(valEcuaciones)



  
  
  # print("MULTIPLICACIÓN")
  # multi = np.dot(L,m1)
  # print(multi)


# ejercicico 3
def ejer3():
  # descomposición LU sin pivoteo parcial
  def ejerA():

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

    # declaration of variables

    A = [
      [8,4,-1],
      [-2,5,1],
      [2,-1,6]
    ]
    equationsValues = [
      11,4,7
    ]
    n = len(A)
    L = createMatriz(len(A))
    
    # verificar que la matriz es cuadrada
    if len(A) != len(A[0]):
      return print("La matriz no es una cuadrada")

    # sin pivoteo (sin intercambio de filas)
    for j in range(len(A)):
      for i in range(len(A)):
        if i == j:
          pMatriz = A[i]
          pivo = A[i][j]
        if i > j:
          L[i][j] = A[i][j]/pivo
          newAList = list(map(lambda x: x*(A[i][j]/pivo) , pMatriz))
          A[i] = list(map(lambda x,y: x-y , A[i],newAList));
    
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
  ejerA();

  def ejerB():
    # calcular la inversa de la matriz
    # 1. calcular la determinante de la matriz
    # 2. si la determinante es 0, entonces no tiene matriz inversa
    # 3. luego la transpuesta de la matriz
    # 4. matriz adjunta
    # paso 1

    A = [
      [8,4,-1],
      [-2,5,1],
      [2,-2,6]
    ]
    trans = np.zeros((3,3));
    mInve = np.zeros((3,3));

    # En este caso vamos a utilizar el try except para detectar los errores
    try:
      # hallar la determinante
      det = np.linalg.det(A)
    
      if det != 0:
        # calcular la trasnpuesta 
        for i in range(len(A)):
          for j in range(len(A[0])):
            trans[j][i] = A[i][j];

        # matriz adjunta

        def matrixCof(i,j):
          mx = []
          for k in range(len(trans)):
            b = []
            for p in range(len(trans[0])):
              if (i != k and j != p):
                b.append(trans[k][p])
            if len(b) != 0:
              mx.append(b)
          print(mx)
          return mx

        for i in range(len(trans)):
          for j in range(len(trans[0])):
            mInve[i][j] = round((((-1)**(i+j)) * np.linalg.det(matrixCof(i,j)))/det,2)
      else: 
        print("No tiene inversa")
    except:
      print("No tiene inversa")
    print(mInve)

    def multiplyMatrix(matrix1, matrix2):
      s = 0
      f1 = []
      for i in range(len(matrix1)):
        f2 = []
        for j in range(len(matrix2)):
            for k in range(len(matrix1[0])):
              s = s + (matrix1[i][k] * matrix2[k][j]);
            f2.append(round(s,1))
            s = 0
        f1.append(f2)
      return f1;         
    # demostración [A][A^-1] = [I] 
    print(multiplyMatrix(A,mInve))
  ejerB();



ejer3();



# simple gaussian method
def methodGaussSimple(A):
  # tamaño de la matriz
  n = len(A)

  # eliminación hacia adelante
  # recorrido por columna
  for j in range(n):
    for i in range(n):
      if i == j:
        pivoMatriz = A[i];
        pivo = A[i][j];

      if i>j:
        newAList = list(map(lambda x: x*(A[i][j]/pivo) , pivoMatriz))
        A[i] = list(map(lambda x,y: x-y , A[i],newAList));
  # sustitución hacia atrás 
  # calcular los valores del sistema de ecuaciones
  valEcuaciones = []
  for i in reversed(range(n)):
    sum = A[i][n];
    print(f"i")
    for j in reversed(range(i+1,n)):
      print(n-j-1)
      sum = sum - A[i][j]*valEcuaciones[n-j-1];
    valEcuaciones = [*valEcuaciones, sum/A[i][i]]
  
  # devolver el valor de las ecuaciones
  return valEcuaciones;









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
ejer2();



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









import cmath;
from decimal import Decimal
from numpy import size
from sympy import *;
import numpy as np
# ejercicio 9.1
def EjerMatrices():
  # calcular la transpuesta de una matriz
  mNormal = [
  [1,0,3],
  [1,-5,3],
  [1,0,3],
  [1,-5,3]
  ];

  # objetivo a lograr
  # [1,1],
  # [2,2],
  # [3,3]

  mTrapuesta = [];
  # calculo
  lista = [];
  c1 = 0;
  while(c1 < len(mNormal[0])):
    for i in range(len(mNormal)):
      lista.append(mNormal[i][c1]);
    mTrapuesta.append(lista);
    c1 += 1;
    lista = [];
  # mostrar nuevo array  
  print(mTrapuesta);

# 9.2 ejercicios
def Ejer2A():
  # calcular las dimensiones de las matrices
  A = [
    [1,5,8],
    [7,2,3],
    [4,0,6]
  ]
  B = [
    [1],
    [7]
  ]
  C = [
    [7,2,3]
  ]
  D=[]
  E=[]
  F=[]
  G=[]
  # calcular la longitud de la matriz
  def sizeMatriz(matriz):
    print(f"Size: {len(matriz)}x{len(matriz[0])}")
  # que tipo de matriz es
  def typeMatriz(matriz):
    if len(matriz) == len(matriz[0]):
      print("La matriz es cuadrada.");
    elif len(matriz) == 1:
      print("Es una matriz reglón");
    elif len(matriz[0]) == 1:
      print("Es una matriz columna");


def gaussJordanMatrices():
  A = [
    [1,2,1,8],
    [-1,3,-2,1],
    [3,4,-7,10]
  ];
  # tamaño de la matriz
  n = len(A);

  # eliminación hacia adelante
  for j in range(n):
    for i in range(n):
      if i == j:
        # elementos de la fila del pivote
        pivoMatriz = A[i];
        # elemento del pivote (i,j)
        pivo = A[i][j];

      if i>j:
        # factor = {A[i][j]}/{pivo}
        newAList = list(map(lambda x: x*(A[i][j]/pivo) , pivoMatriz))
        # se remplaza la nueva lista en toda la fila
        A[i] = list(map(lambda x,y: x-y , A[i],newAList));
  
  # imprimir la matriz
  for i  in range(len(A)):
    print(A[i]);
  
  # sustitución hacia atrás
  valEcuaciones = []
  # calculamos el primer valor
  for i in reversed(range(n)):
    sum = A[i][n];
    for j in reversed(range(i+1,n)):
      sum = sum - A[i][j]*valEcuaciones[j-n];
    valEcuaciones = [sum/A[i][i],*valEcuaciones]
  
  print(valEcuaciones);


# método de eliminación de gauss simple
def methodGaussSimple():
  A = [
    [3,-0.1,-0.2,7.85],
    [0.1,7,-0.3,-19.3],
    [0.3,-0.2,10,71.4]
  ];

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
  print(valEcuaciones)

def methodGaussPivoteoParcial():
  A = [
    [0.1,-2,-1,-14],
    [0,3,1,1],
    [3,1,-1,1]
  ];
  # tamaño de la matriz
  n = len(A)

  # eliminación hacia adelante
  # recorrido por columna
  for j in range(n):
    for i in range(n):
      if i == j:
        pivoMatriz = A[i];
        pivo = A[i][j];
        
        # encontrar el pivo mayor de toda la columna
        pos = 0
        for k in range(n):
          if k>i:
            if abs(pivo) < abs(A[k][i]):
              pivo = A[k][i]
              pos = k;
        if pos != 0:
          pivoMatriz = A[pos]
          pivo = A[pos][i]
          # cambios de fila
          aux = A[pos];
          A[pos] = A[i];
          A[i] = aux;
        print(A)
      if i>j:
        newAList = list(map(lambda x: x*(A[i][j]/pivo) , pivoMatriz))
        A[i] = list(map(lambda x,y: x-y , A[i],newAList));
methodGaussPivoteoParcial();


# gauus con pivoteo parcial
# gauss jordan


# método de eliminación gaussiana con pivoteo parcial


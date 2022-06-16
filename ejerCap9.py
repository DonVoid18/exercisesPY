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
    [3,6,-2,9,6],
    [-5,4,5,-6,5],
    [-3,8,2,-3,3],
    [-4,10,3,9,9],
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
  print(A)
  
  # sustitución hacia atrás
  valEcuaciones = []
  # calculamos el primer valor
  for i in reversed(range(n)):
    sum = A[i][n];
    for j in reversed(range(i+1,n)):
      sum = sum - A[i][j]*valEcuaciones[j-n];
    valEcuaciones = [sum/A[i][i],*valEcuaciones]
  
  print(valEcuaciones);
gaussJordanMatrices();
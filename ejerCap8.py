# LIBRERÍAS UTILIZADAS
from sympy import *;

# ejercicios del cap 8
# ejercicio 1

def ejer1():
  v = Symbol("v")
  a = 12.02
  b = 0.08407
  n = 1
  R = 0.082054
  T = 400
  P = 2.5

  # error admitido 
  ea = 0.001
  it = 1

  v0 = (n*R*T)/(P)
  fPrincipal = (P+(a/v**2))*(v-b)-R*T

  while(True):
    # función principal
    f1 = sympify(fPrincipal).subs(v,v0)
    
    # función principal derivada
    f2 = sympify(diff(fPrincipal),v).subs(v,v0)

    vr = v0 - (f1/f2)
    e = abs((vr-v0)/vr)*100

    v0 = vr

    print(f"it:{it} - valor: {vr} - error: {e}")

    if e < ea:
      break 
    it = it + 1

ejer1()
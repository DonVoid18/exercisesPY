# librerías 
from sympy import *;
def optimizacion():
  # definición de variables
  a, b = symbols('a b', real=True)
  
  # función principal
  # f = input("Función: ")
  f = -3*(20*a-400)**2-(6/7)*(2*b-44)**2+8

  # hallar los puntos críticos
  def pCriticos():
    # derivda parcial respecto "a"
    a1 = solve(Eq(diff(f,a),0))
    # derivda parcial respecto "b"
    b1 = solve(Eq(diff(f,b),0))
    # función evaluado con los puntos críticos
    vf = f.subs({a: a1[0], b: b1[0]})
    return a1,b1,vf    
  
  def dHessiano():
    a2 = diff(diff(f,a),a)
    b2 = diff(diff(f,b),b)
    ab2 = diff(diff(f,a),b)
    ba2 = diff(diff(f,b),a)

    op = (a2*b2)-(ab2*ba2)
    
    if op > 0:
      if a2 > 0:
        print("El punto crítico es mínimo.")
      else:
        print("El punto crítico es máximo.")
    elif op == 0:
      print("Existencia indeterminado")
    else:
      print("El punto crítico es un punto de silla.")

  ptc = pCriticos()
  # pregunta 1
  print(f"a = {ptc[0]}, b = {ptc[1]}")
  # pregunta 2
  print(f"Resultado promedio óptimo: {ptc[2]}")
  # pregunta 3
  print("¿El óptimo es un mínimo, máximo o punto de silla?")
  dHessiano()
def gEjer():
  from sympy.plotting import plot3d
  x, y = symbols('x y')
  plot3d(-3*(20*x-400)**2-(6/7)*(2*y-44)**2+8, (x, -1000, 1000), (y, -1000, 1000))
gEjer()

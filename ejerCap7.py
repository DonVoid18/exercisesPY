# bibliotecas
import cmath;
from decimal import Decimal
from traceback import format_tb
from sympy import *;
# ejercicio 7.3 método de muller
def metodoMuller():
    # declaramos las varibles que utilizamos
    x = Symbol("x");

    # función que calcule los valores de las funciones fx0, fx1, fx2 
    def valueFunction(number):
        value = sympify(fPrincipal).subs(x,number);
        return complex(value);
    
    # ingresamos la función principal a evaluar
    fPrincipal = input("Función: ");

    # tenemos que ingresar 3 valores que vienen a ser x0 x1 x2 y luego calculamos x3
    x0 = float(input("Valor x0: "));
    x1 = float(input("Valor x1: "));
    x2 = float(input("Valor x2: "));
    
    # también necesitamos el error máximo para que pueda para la iteración
    eMax = float(input("Error máximo: "));
    print("x3 --- error");
    it = 0;
    while(True):
        # necitamos la función principal de donde queremos calcular la raíz aproximada
        f0 = valueFunction(x0);
        f1 = valueFunction(x1);
        f2 = valueFunction(x2);

        h0 = x1 - x0;
        h1 = x2 - x1;

        d0 = (f1-f0)/(h0);
        d1 = (f2-f1)/(h1);

        a = (d1-d0)/(h1+h0);
        b = a*(h1)+d1;
        c = f2;

        denominador = 0;
        discri = b**2-4*a*c;
        
        if abs(b+cmath.sqrt(discri)) > abs(b-cmath.sqrt(discri)):
            denominador = b+cmath.sqrt(discri);
        else:
            denominador = b-cmath.sqrt(discri);
        x3 = x2 + (-2*c)/denominador;
        
        # error
        e = abs((x3-x2)/(x3))*100;
        it = it + 1;
        print(it,round(x3.real,3),round(Decimal(x3.imag),6),"i",round(e,3));
        if e<eMax:
            break;
        
        # siguiente iteración
        x0 = x1;
        x1 = x2;
        x2 = x3;
metodoMuller();
# def pruebasOperaciones():
#     fx = input("función: ");
#     def valueFunction(xtype = 2):
#         k = sympify(fx).subs(x,xtype);
#         return k;
#     x,x0,x1,x2 = Symbol("x x0 x1 x2");
#     print(valueFunction());
def raicesIm():
    # tenemos que ingresar 3 valores que vienen a ser x0 x1 x2 y luego calculamos x3
    x0 = float(input("Valor x0: "));
    x1 = float(input("Valor x1: "));
    x2 = float(input("Valor x2: "));
    
    # también necesitamos el error máximo para que pueda para la iteración
    eMax = float(input("Error máximo: "));
    print("x3 --- error");
    while(True):
        # necitamos la función principal de donde queremos calcular la raíz aproximada
        # f0 = 2*x0**4+6*x0**2+10;
        # f1 = 2*x1**4+6*x1**2+10;
        # f2 = 2*x2**4+6*x2**2+10;
        f0 = x0**3-x0**2+3*x0-2
        f1 = x1**3-x1**2+3*x1-2
        f2 = x2**3-x2**2+3*x2-2

        h0 = x1 -x0;
        h1 = x2 -x1;

        d0 = (f1-f0)/(h0);
        d1 = (f2-f1)/(h1);

        a = (d1-d0)/(h1+h0);
        b = a*(h1)+d1;
        c = f2;
        denominador = 0;
        discri = b**2-4*a*c;
        print(discri);
        if abs(b+cmath.sqrt(discri)) > abs(b-cmath.sqrt(discri)):
            denominador = b+cmath.sqrt(discri);
        else:
            denominador = b-cmath.sqrt(discri);
        print(denominador);
        
        x3 = x2 + (-2*c)/denominador;
        
        # error
        e = abs((x3-x2)/(x3));
        if e<eMax:
            break;
        
        # siguiente iteración
        x0 = x1;
        x1 = x2;
        x2 = x3;


# método de beirstow
def metodoBeirtow():
    x = Symbol("x");
    valuesA = [];
    valuesB = [];
    valuesC = [];

    deltaR = 0;
    deltaS = 0;
    
    er = 1;
    es = 1;
    eInicial = 0.01;
    # 1% = 0.01
    # estos valores deben ingresarse por consola (ojo: en caso de que un error se deben cambiar los valores de r y s)
    r = -1;
    s = -1;
    fPrincipal = input("Función: ");

    # los coeficientes del polinomio
    valuesA = Poly(fPrincipal, x).all_coeffs();
    # grado mayor del polinomio por ejemplo x2 +x +1 + x gradoMax = cantidad - 1
    n = len(valuesA)-1;
    # contador de iteraciones
    contador = 1;
    print("RAICES CON EL CÁLCULO BEIRSTOW")
    while(true):
        # calcular los valore de b
        for i in range(n+1):
            if i == 0:
                valuesB.append(valuesA[i]);
            elif i == 1:
                valuesB.append(valuesA[i]+valuesB[i-1]*r);
            else:
                valuesB.append(valuesA[i]+r*valuesB[i-1]+s*valuesB[i-2]);
        for i in range(n):
            if i == 0:
                valuesC.append(valuesB[i]);
            elif i == 1:
                valuesC.append(valuesB[i]+valuesC[i-1]*r);
            else:
                valuesC.append(valuesB[i]+r*valuesC[i-1]+s*valuesC[i-2]);
       # ahora calculamos los deltas
        deltaR = float(-valuesB[n-1]*valuesC[n-2]+valuesB[n]*valuesC[n-3])/float((valuesC[n-2])**2-valuesC[n-1]*valuesC[n-3]);
        deltaS = float(-valuesB[n]*valuesC[n-2]+valuesB[n-1]*valuesC[n-1])/float((valuesC[n-2])**2-valuesC[n-1]*valuesC[n-3]);
        # calculamos los errores
        er = abs(deltaR/(deltaR+r));
        es = abs(deltaS/(deltaS+s));
        # nuevos valores de r y s
        r = deltaR + r;
        s = deltaS + s;

        # con los nuevos valores podemos calcular el valor de la raíces
        # x^2-rx-s
        
        if er < eInicial and es < eInicial:
            contador = 0;
            # raices de la ecuación
            x1 = (-(-r)+sqrt((-r)**2-4*(-s)))/2;
            x2 = (-(-r)-sqrt((-r)**2-4*(-s)))/2;
            print(round(x1,1));
            print(round(x2,1));
            valuesA = valuesB[:-2];
            n = len(valuesA)-1;
            
            # si es grado dos entonces calculamos las 2 últimas raíces y se hace un brak
            if n==2:
                print(round((-valuesA[1]+sqrt(valuesA[1]**2-4*valuesA[0]*valuesA[2]))/(2*valuesA[0]),1));
                print(round((-valuesA[1]-sqrt(valuesA[1]**2-4*valuesA[0]*valuesA[2]))/(2*valuesA[0]),1));
                break;
            elif n==1:
                print(round(-valuesA[1]/valuesA[0],1));
                break;
            # si es grado uno entonces calculamos la 1 última raíz
        # aumentar el contador
        contador = contador + 1;

        # reiniciar los valores de los arrays
        valuesB = [];
        valuesC = [];
metodoBeirtow();

def raicesDeUna():
    print("RAICES CON EL MÉTODO SOLVE")
    x, y, z, t = symbols('x y z t')
    for i in solve(x**10-3.5*x**4+2.75*x**3+2.125*x**2-3.875*x+1.25, x):
        print(f"{i}");
raicesDeUna();
#para hallar todas las raíces
# x, y, z, t = symbols('x y z t')
    # r = s = 1;
    # print(solve(x**5-3.5*x**4+2.75*x**3+2.125*x**2-3.875*x+1.25, x));

import matplotlib.pyplot as plt
def limites():
    x = symbols("x");
    value = limit(x**2-x+2,x,2);
    print(value);


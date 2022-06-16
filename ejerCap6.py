import math
from decimal import Decimal
from sympy import *;

# ejercicio 6.1
def metodoPuntoFijo():

    xInicial = float(input("Ingrese el valor inicial: "));
    eInicial = float(input("Ingrese el error E(a): "));
    it = 1;

    print("it       xi         g(x)       error     error(%)");
    while(True):
        # aquí tenemos el g(x)
        xr = 2*math.sin(math.sqrt(xInicial));
        e = abs((xr - xInicial)/xr);

        # imprimir la lista de valores
        print(f"{it} --- {round(Decimal(xInicial),6)} --- {round(Decimal(xr),6)} --- {round(Decimal(e),6)} --- {round(Decimal(e),6)*100}%");

        xInicial = xr;
        it = it + 1;

        # termina cuando el error es menor igual que el error del problema

        if round(Decimal(e),5) <= eInicial:
            print(f"Raiz aproximada: {round(Decimal(xInicial),6)} con un error de {round(Decimal(e),6)*100}%");
            break;
# ejercicio 6.4
def metodoNewtonRaphson():
    x = Symbol("x");
    fPrincipal = input("función: ");
    xInicial = float(input("Ingrese el valor inicial: "));
    eInicial = float(input("Ingrese el error E(s): "));

    it = 1;

    print("it         xi         xi+1         f(x)         f'(x)         e(s)");
    while(True):

        # f(x)
        # f1 = -1+5.5*xInicial-4*(math.pow(xInicial,2))+0.5*(math.pow(xInicial,3))
        f1 = sympify(fPrincipal).subs(x,xInicial);
        # f'(x)
        # f2 = 5.5 - 8*xInicial+1.5*(math.pow(xInicial,2));
        f2 = sympify(diff(fPrincipal),x).subs(x,xInicial);
        
        xr = xInicial - (f1/f2);
        e = abs((xr - xInicial)/xr)*100;

        # imprimir los valores
        print(f"{it} --- {round((xInicial),6)} --- {round((xr),6)} --- {round((f1),6)} --- {round((f2),6)} --- {round((e),6)}%");

        xInicial = xr;
        it = it + 1;

        # termina cuando el error es menor que el error del problema
        if round((e),5) < eInicial:
            print(f"Raiz aproximada: {round((xInicial),6)} con un error de {round((e),6)}%");
            break;
# 6.2 en la secante
def metodoSecante():
    xInicial0 = float(input("Ingrese el valor de xi-1: "));
    xInicial1 = float(input("Ingrese el valor de xi: "));
    

    # Como nos da el númuero de iteraciones entonces no es necesario tener el error
    # eInicial = float(input("Ingrese el error: "));

    it = 1;

    print("it         xi-1         xi         xi+1         f(xi)         f(xi-1)         error         error(%)");
    while(True):
        f1 = 2*math.pow(xInicial1,3)-11.7*math.pow(xInicial1,2)+17.7*xInicial1-5;
        f2 = 2*math.pow(xInicial0,3)-11.7*math.pow(xInicial0,2)+17.7*xInicial0-5;
        
        xr = xInicial1 - ((f1*(xInicial1-xInicial0))/(f1 - f2));
        e = abs((xInicial1 - xInicial0)/xInicial1);

        # imprimir la lista de valores
        print(f"{it} --- {round(Decimal(xInicial0),6)} --- {round(Decimal(xInicial1),6)} --- {round(Decimal(xr),6)} --- {round(Decimal(f1),6)} --- {round(Decimal(f2),6)} --- {round(Decimal(e),6)} --- {round(Decimal(e),6)*100} %");

        xInicial0 = xInicial1;
        xInicial1 = xr;
        it = it + 1;

        # termina cuando el error es menor que el error del problema

        if it==4:
            print(f"Raiz aproximada: {round(Decimal(xr),6)} con un error de {round(Decimal(e),6)*100}%");
            break;


# ejercicio 2.12 metodo de la secante modicado
def metodoSecanteModificado():
    x1 = float(input("Ingrese el valor de x1 o valor inicial: "));
    d = float(input("Ingrese el valor del delta: "));
    eInicial = float(input("Ingrese el error: "));
    i = 1;
    
    while(True):
        xd = x1+(d*x1);

        # función principal
        f1 = x1**(3.5)-80;
        fd = xd**(3.5)-80;

        xr = x1 - ((d*x1*f1)/(fd - f1));

        e = abs((xr-x1)/xr)*100; 

        print(f"Iteración: {i}    {round(Decimal(x1),6)}     {round(Decimal(xd),6)}      {round(Decimal(xr),6)}    {round(Decimal(f1),6)}     {round(Decimal(fd),6)}     {round(Decimal(e),6)}");
        i = i + 1;
        x1 = xr;
        if round((e),5) < eInicial:
           break;
metodoSecanteModificado();
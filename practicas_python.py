# OPERADORES ARITMÉTICOS

def operadoresArimeticos():
    num1 = 5;
    num2 = 10;
    resultado = num1 + num2;

    print(resultado);
# "*" = multi
# / = division
# "//"" = division entera a la baja
# "%" = módulo (residuo)
# "**" = exponente

# OPERADORES RELACIONALES
def operadoresRelaciones():
    resultado = 20 > 10;
    print(resultado);


# OPERADORES LÓGICOS
def operadoresLogicos():
    # and or not
    a = 10;
    b = 15;
    c = 20;
    resultado = ((a < b) and (b > c));
    print(resultado);


# OPERADORES DE ASIGNACIÓN
def operadoresAsignacion():
    a = 10;
    a += 10;# suma de asignación
    a -= 5; # resta de asignación
    a *= 2; # multiplicación de asignación

    print(a);

# SALIDAS   

def salidas():
    nombre = "angelo";
    edad = 18;

    print("Hola mi nombre es ",nombre," y tengo ",edad," años");    
    print("Hola mi nombre es {} tengo {} años".format(nombre, edad));
    print(f"Hola mi nombre es {nombre} y tengo {edad} años");


# ENTRADA DE DATOS

def entradas():
    numero = int(input("Digite un número: "));

    nombre = input("Ingrese su nombre: ");

    print(f"Tu nombre es {nombre}");
    print(f"Esta variable es de tipo {type(numero)} y su valor es {numero}");

# FUNCIONES INTEGRADAS
def funcionesIntegradas():
    n = int("10");
    a = str(10.2);
    binario = bin(10);
    hexa = hex(100);

    decimal = int("0b1010", 2);
    print(f"{binario} - {hexa}");
    print(f"Decimal: {decimal}");


# EJERCICIO 1   
def ejercicio1():
    a = float(input("Ingrese el primer número: "));
    b = float(input("Ingrese el segundo número: "));
    c = float(input("Ingrese el tercar número: "));

    operation = (a**3 * (b**2 - 2*a*c))/(2*b);
    print(f"El resultado es: {operation}");

# EJERCICIO 2
def ejercicio2():
    a = float(input("a ->"));
    b = float(input("b ->"));
    
    operation = (((3+5*8)<3) and (((-6/3)*4)+2 < 2)) or (a>b);
    print(f"Resultado de la operación lógica: {operation}");

# EJERCICIO 3
def ejercicio3():
    a = float(input("a ->"));
    b = float(input("b ->"));
    aux = a;
    a = b;
    b = aux;

    print(f"Los valores son a-{a} b-{b}");

# EJERCICIO 4
from math import factorial, pi
from pickle import FALSE, TRUE
from re import M
import re
from tokenize import Double;
def ejercicio4():
    radio = float(input("Ingrese el valor del radio: "));
    area = pi * radio**2;
    longitud = 2 * pi * radio;

    print(f"El área del circulo es: {area}");
    print(f"Longitud del circulo: {longitud}");




# EJERCICIO 5
def ejercicio5():
    monto = float(input("Ingrese el monto total de su compra: "));
    montoFinal = monto - (monto * 15/100);

    print(f"El monto final a pagar es: {montoFinal:.2f}");


# CONDICIONALES

def postOnega():
    numero = int(input("Ingrese un número: "));

    if(numero > 0):
        print("El número es positivo");
    elif (numero == 0):
        print("El número es cero");
    else:
        print("El número no es positivo");


# CONDICIONALES ANIDADOS

def condicionesAnidados():
    edad = int(input("Ingrese su edad: "));
    if(0<edad<100):
        print("Edad correcta");
        if(edad >= 18):
            print("Es mayor de edad");
        else:
            print("No es mayor de edad");
    else:
        print("Edad incorrecta");


# EJERCICIOS CONDICIONALES

def condicionales1():
    num1 = float(input("Ingrese el primer número: "));
    num2 = float(input("Ingrese el segundo número: "));
    
    if(num1%2 == 0 and num2%2 == 0):
        print("Ambos números son pares");
    elif(num1%2 != 0 and num2%2 == 0):
        print(f"El {num2} es par");
    elif(num1%2 == 0 and num2%2 != 0):
        print(f"El {num1} es par");
    else:
        print("Ambos números son impares");

# ejercicio 2
def condicionales2():
    num1 = float(input("Ingrese el número 1: "));
    num2 = float(input("Ingrese el número 2: "));
    num3 = float(input("Ingrese el número 3: "));

    if(num1 > num2 and num1 > num3):
        print(f"El número {num1} es el mayor");
    elif(num2 > num1 and num2 > num3):
        print(f"El número {num2} es el mayor")
    elif(num3 > num1 and num3 > num2):
        print(f"El número {num3} es el mayor")
    elif(num3 == num2 == num1):
        print("Los tren números son iguales");

#ejercicio 3
def condicionales3():
    vocal = input("Ingrese un letra: ").lower();
    if(vocal == "a" or vocal == "e" or vocal == "i" or vocal == "o" or vocal == "u"):
        print(f"{vocal} es una vocal");
    else:
        print(f"{vocal} no es una vocal");

# ejercicio 4
def condicionales4():
    num1 = float(input("Ingrese el primer número: "));
    num2 = float(input("Ingrese el segundo número: "));
    operador = input("suma(s-S), resta(r-R), multi(p-P-m-M), divi(d-D): ").lower();
    
    if(operador == "s"):
        return num1 + num2;
    elif(operador == "r"):
        return num1 - num2;
    elif(operador == "p" or operador == "m"):
        return num1 * num2;
    elif(operador == "d" or operador == "D"):
        return num1 / num2;
    else:
        return("Se equivocó de operación");

def condicionalesSegunda1():
    num1 = float(input("Ingrese el primer número: "));
    num2 = float(input("Ingrese el segundo número: "));
    
    operador = input("suma(s-S), resta(r-R), multi(p-P-m-M), divi(d-D): ").lower();
    if(operador == "s"):
        suma = num1 + num2;
        print(f"La suma de {num1} + {num2} = {suma}");
    elif(operador == "r"):
        resta = num1 - num2;
        print(f"La resta de {num1} - {num2} = {resta}");
    elif(operador == "p" or operador == "m"):
        multi = num1 * num2;
        print(f"La multiplicación de {num1} * {num2} = {multi:.2f}");
    elif(operador == "d"):
        divi = num1 / num2;
        print(f"La división de {num1} / {num2} = {divi:.2f}");

# ejercicio 5

def condicionales5():
    print("\t---Menu---");
    print("1. Ingresar dinero a la cuenta");
    print("2. Retirar dinero de la cuenta");
    print("3. Mostrar dinero disponible");
    print("4. Salir");

    option = int(input("Ingrese una opción: "));
    saldoI = 1000;
    if(option == 1):
        ingreso = float(input("Dinero a ingresar: "));
        saldoI = saldoI + ingreso;
        print(f"Tu nuevo saldo es: {saldoI} $");
    elif(option == 2):
        retiro = float(input("Dinero a retirar: "));
        if(retiro < saldoI):
            saldoI = saldoI - retiro;
            print(f"Tu nuevo saldo es: {saldoI} $");
        else:
            print("El retiro superé a la cantidad en la cuenta");
    elif(option == 3):
        print(f"El saldo actual de tu cuenta es {saldoI} $");
    elif(option == 4):
        print("Saliendo del cajero");
    else:
        print("Seleccione correctamente una opción");

# BUCLES WHILE

def blucles1():
    import math;
    numero = int(input("Ingrese un número: "));
    while(numero < 0):
        print(f"El número {numero} es negativo");
        numero = int(input("Ingrese un número: "));
    print("El número es positivo");


def bucles2():
    i = 0;
    while(i<10):
        print(f"{i}-angelo");
        i += 1;
    print("Terminó");

# bucle for

def buclesFor1():
    coleccion = [1,2,3,4,5];
    diccionario = {"angelo": 22, "rios": 15, "jouse": 12};

    for clave, valor in diccionario.items():
        print(f"{clave} - {valor}");

def buclesFor2():
    nombre = "angelo";
    for i in nombre:
        print(f"{i}", end="");


#  bucles de tipo range
def buclesRange():
    for i in range(5):
        print("angelo");
    for a in range(5,-1):
        print(f"{a}");
    for b in range(2,21,2):
        print(f"{b}");

# CONTINUE AND BREAK

def propiedades():
    for i in range(10):
        if( i == 3):
            continue;
        print(f"{i}");


# ejercicios de bucles
def ejerBucles1():
    lista = [];
    for i in range(1, 51):
        lista.append(i);

    for i in lista:
        print(i, end=" - ");


# una sola linea lista = list(range(1,51));

def ejerBucles2():
    lista = [];
    lista = list(range(1, 11));

    valorMulti = float(input("Ingrese el número: "));
    print(lista);
    contador = 0; 
    for i in lista:
        lista[contador] *= valorMulti;
        contador += 1;
    print(lista);

def ejerBuclesSegundaParte():
    lista = [];
    lista = list(range(1, 11));

    valorMulti = float(input("Ingrese el número: "));
    print(lista);
    for index, i in enumerate(lista):
        lista[index] = i * valorMulti;
    print(lista);

# ejercicio 3 de bucles


def ejerBucles3():
    lista = [];
    
    while(True):
        valor = float(input("Ingrese un número: "));
        if valor != 0:
            lista.append(valor);
        else:
            lista.sort();
            print(f"La lista actualiza es: {lista}");
            break;
        

# ejercicio 4 
def ejerBucles4():
    inicio = int(input("Ingrese el inicio del rango: "));
    final = int(input("Ingrese el final del rango: ")); 
    suma = 0;
    for i in range(inicio, final + 1):
        if(i%2 == 0):
            suma = suma + i;

    print(f"[{inicio},{final}] = {suma}");


# ejercicio 5
def ejerBucles5():
    number = int(input("Ingrese el número: "));
    factorial = 1;
    if number != 0:
        for i in range(1,number + 1):
            factorial = factorial * i;
            print(f"{i} != {factorial}");
    else:
        print(f"El factorial de {number} es 0")
    print(f"El factorial de {number} es: {factorial}");

# ejercicio 6
def ejerBucles6():
    number = int(input("Ingrese el número para multiplicar: "));
    tabla = [];
    for i in range(11):
        tabla.append(i * number);
    print(tabla);


# ejercicio 7
def ejerBucles7():
   import random;
   ale = random.randrange(1, 101);
   encontrado = False;
   intentos = 0;
   while(not(encontrado)):
        intentos += 1;
        numberUser = float(input("Ingrese un número: "));
        if(numberUser > ale):
           print("Bajale un pco");
        elif(numberUser < ale):
            print("subele un poco");
        elif(numberUser == ale):
            print(f"Encontraste el número - cant. intentos: {intentos}");
            encontrado = True;



# ejercicio 8
def ejerBucles8():
    saldo = float(input("Ingrese el saldo inicial: "));
    print("1.Ingresar dinero en la cuenta");
    print("2. Retirar el dinero de la cuenta");
    print("3. Mostrar el dinero de la cuenta");
    print("4. Salir");
    while(True):
        opcion = int(input("Ingrese una opción: "));
        if opcion == 1:
            ingreso = float(input("Cuando dinero va ingresar: "));
            saldo += ingreso;
            print(f"Nuevo saldo es: {saldo}"); 
        elif opcion == 2:
            retiro = float(input("Cuánto dinero va retirar: "));
            if retiro > saldo:
                print("El retiro es mayor que el saldo actual");
            else:
                saldo -= retiro;
            print(f"Nuevo saldo es: {saldo}"); 
        elif opcion == 3:
            print(f"El dinero de la cuenta es: {saldo}")
        elif opcion == 4:
            print(f"Saliendo");
            break;
        else:
            print("No elijio una opción");

# ejercicio 9

def ejerBucles9():
    texto = input("Ingrese un texto");
    texto2 = "";
    for i in texto:
        if i != " ":
            texto2 = texto2 + i;
    print(f"Nuevo texto {texto2}, longitud: {len(texto2)}");

# ejercicio 10

def ejerBucles10():
    cadena = input("Ingrese un texto: ");
    lista = [];
    for i in cadena:
        if i not in lista:
            lista.append(i);
    print(f"La nueva lista es {lista}");
ejerBucles10();
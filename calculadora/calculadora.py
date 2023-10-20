
#Metodo para imprimir el menu
def printMenu():
    print("BIENVENIDO A LA CALCULADORA:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Es par")
    print("6. Mayor")
    print("7. Salir")

#Definicion de variables
number1 = int
number2 = int

#Metodo para preguntar los números a operar
def askNumbers():
    global number1
    number1 = int(input("Introduce el primer número: "))
    global number2
    number2 = int(input("Introduce el segundo número: "))

#Metodo para definir si un número es par o no 
def ifPar():
    numberpar = int(input("Introduce un numero para comprobar si es par: "))
    print("El número  " + str(numberpar) + " es par ") if numberpar % 2 == 0 else print("El número  " + str(numberpar) + " no es par ")

def mayorQue():
    askNumbers()
    if number1 > number2:
        print("El número " + str(number1) + " es mayor que " + str(number2))
    else:
        print("El número " + str(number1) + " es menor que " + str(number2))

while True:
    printMenu()
    opt = int(input(""))
    if opt == 1:
        askNumbers()
        print("La suma de " + str(number1) + " + " + str(number2) + " = " + str(number1+number2))
    elif opt == 2:
        askNumbers()
        print("La resta de " +  str(number1) + " - " + str(number2) + " = " + str(number1 - number2))
    elif opt == 3:
        askNumbers()
        print("La multiplicacion de " +  str(number1) + " + " + str(number2) + " = " + str(number1 + number2))
    elif opt == 4:
        askNumbers()
        print("La division de " +  str(number1) + " / " + str(number2) + " = " + str(number1 / number2))
    elif opt == 5:
        ifPar()
    elif opt == 6:
        mayorQue()
    elif opt == 7 or opt > 7 or opt < 1:
        break


#Metodos para test unitarios 

#Sumar
def sumar(numero1, numero2):
    return numero1 + numero2
#Restar
def restar(numero1, numero2):
    return numero1 - numero2
#Multiplicar
def multiplicar(numero1, numero2):
    return numero1 * numero2
#Dividir
def dividir(numero1, numero2):
    return numero1 / numero2

#Comprobar si numero es par
def comprobarPar(numero1):
    return True if numero1 % 2 == 0 else False
#Comprobar numero mayor
def comprobarMayores(numero1, numero2):
    return True if numero1 > numero2 else False



#Metodo para imprimir el menu
def printMenu():
    print("BIENVENIDO A LA CALCULADORA:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

#Definicion de variables
number1 = int
number2 = int

#Metodo para preguntar los números a operar
def askNumbers():
    global number1
    number1 = int(input("Introduce el primer número: "))
    global number2
    number2 = int(input("Introduce el segundo número: "))


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
    elif opt == 5 or opt > 5 or opt < 1:
        break
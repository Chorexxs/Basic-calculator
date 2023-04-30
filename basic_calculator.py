# Primero hay que definir las funciones: suma, resta, multiplicación y división

def Suma(a, b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer) + "\n")


def Resta(a, b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer) + "\n")


def Multiplicacion(a, b):
    answer = a * b
    print(str(a) + " * " + str(b) + " = " + str(answer) + "\n")


def Division(a, b):
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer) + "\n")

# Ahora hay que imprimir las opciones para el usuario

# Aquí también hay que poner un loop con while para que el programa se siga
# ejecutando hasta que el usuario elija la opción de cerrar


while True:
    print("A. Suma")
    print("B. Resta")
    print("C. Multiplicación")
    print("D. División")
    print("E. Cerrar")

# Lo siguiente que hay que hacer es crear la variable choice para que el
# usuario pueda escoger qué operación matemática hacer
# (para crear estas opciones se usará la sentencia if y elif)

    choice = input("Elije una opción: ")

    if choice == "a" or choice == "A":
        print("Suma")
        a = int(input("Primer número: "))
        b = int(input("Segundo número: "))
        Suma(a, b)
    elif choice == "b" or choice == "B":
        print("Resta")
        a = int(input("Primer número: "))
        b = int(input("Segundo número: "))
        Resta(a, b)
    elif choice == "c" or choice == "C":
        print("Multiplicación")
        a = int(input("Primer número: "))
        b = int(input("Segundo número: "))
        Multiplicacion(a, b)
    elif choice == "d" or choice == "D":
        print("División")
        a = int(input("Primer número: "))
        b = int(input("Segundo número: "))
        Division(a, b)
    elif choice == "e" or choice == "E":
        print("Cerrando calculadora")
        quit()

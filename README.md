# basic_calculator

# Calculadora básica

Este es un programa de calculadora básica en Python que permite realizar operaciones matemáticas simples como suma, resta, multiplicación y división.

## Funciones

El programa define las siguientes funciones:

### Suma

```python
def Suma(a, b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer) + "\n")
```

La función `Suma` recibe dos números (`a` y `b`) como parámetros, realiza la suma y muestra el resultado en la consola.

### Resta

```python
def Resta(a, b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer) + "\n")
```

La función `Resta` recibe dos números (`a` y `b`) como parámetros, realiza la resta y muestra el resultado en la consola.

### Multiplicación

```python
def Multiplicacion(a, b):
    answer = a * b
    print(str(a) + " * " + str(b) + " = " + str(answer) + "\n")
```

La función `Multiplicacion` recibe dos números (`a` y `b`) como parámetros, realiza la multiplicación y muestra el resultado en la consola.

### División

```python
def Division(a, b):
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer) + "\n")
```

La función `Division` recibe dos números (`a` y `b`) como parámetros, realiza la división y muestra el resultado en la consola.

## Uso

El programa presenta un menú interactivo en un bucle `while` para que el usuario pueda seleccionar una operación matemática. Las opciones del menú son:

- A. Suma
- B. Resta
- C. Multiplicación
- D. División
- E. Cerrar

El usuario debe ingresar la letra correspondiente a la opción deseada. El programa solicitará dos números y realizará la operación seleccionada utilizando las funciones definidas anteriormente.

Si se selecciona la opción "E" o "e" para cerrar, el programa finaliza su ejecución.

---
¡Disfruta de tu calculadora básica!

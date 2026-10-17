def digit_multiplication(s):
    """Procesa una cadena de texto con operaciones, multiplicando los dígitos de cada número y aplicando los signos correspondientes.

    PARAMETERS
    ---
    s (str): La cadena de texto que contiene la expresión con números y operadores (`+` o `-`).

    RETURNS
    ---
    int: Devuelve la variable `total` con el resultado numérico final de la operación acumulada.
    """
    total = 0
    actual = 1
    signo = 1

    for n in f"{s}+":
        if n.isdigit():
            actual *= int(n)  # acumula la multiplicacion de los numeros
        else:
            total += signo * actual  # acumula el total de la multiplicacion
            actual = 1
            signo = 1 if n == "+" else -1  # asigna el signo

    return total


print(digit_multiplication("1+2-3+4"))

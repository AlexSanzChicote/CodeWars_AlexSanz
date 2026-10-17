def even_or_odd(number):
    """Determina si un número entero es par o impar.

    PARAMETERS
    ---
    number (int): El número entero que se va a evaluar.

    RETURNS
    ---
    str: Devuelve la variable `text` con el valor "Even" si el número es par, o "Odd" si es impar.
    """
    text = ""
    if number % 2 == 0:  # si el numero es par, devuelve Even
        text = "Even"
    else:
        text = "Odd"  # si el numero es impar, devuelve Odd
    return text


print(even_or_odd(4))

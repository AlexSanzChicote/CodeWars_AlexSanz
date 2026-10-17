def high_and_low(numbers):
    """Encuentra el número mayor y el menor en una cadena de texto de números separados por espacios.

    PARAMETERS
    ---
    numbers (str): Una cadena de texto que contiene números enteros separados por espacios.

    RETURNS
    ---
    str: Devuelve una cadena de texto con el número mayor y el número menor separados por un guion (ej. "5-1").
    """
    mayor = None
    menor = None
    actual = ""

    for i in numbers + " ":
        if i != " ":
            actual += i  # hace que actual sea igual a i
        else:
            if actual:
                num = int(actual)
                # guarda a mayor y menor
                if mayor is None or num > mayor:
                    mayor = num
                if menor is None or num < menor:
                    menor = num
                actual = ""

    return str(mayor) + "-" + str(menor)


print(high_and_low("1 2 3 4 5"))

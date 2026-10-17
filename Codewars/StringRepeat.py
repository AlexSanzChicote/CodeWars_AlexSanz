def repeat_str(repeat, string):
    """Repite una cadena de texto un número determinado de veces.

    PARAMETERS
    ---
    repeat (int): El número de veces que se desea repetir la cadena.
    string (str): La cadena de texto que se va a repetir.

    RETURNS
    ---
    str: Devuelve el resultado de multiplicar la cadena por el número de repeticiones (`string * repeat`).
    """
    return string * repeat  # devuelve la cadena de texto repetida el numero de veces que se indique


print(repeat_str(3, "a"))

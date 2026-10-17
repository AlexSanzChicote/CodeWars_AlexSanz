def switch_it_up(numero):
    """Convierte un número entero (del 0 al 9) en su representación escrita en inglés.

    PARAMETERS
    ---
    numero (int): El número entero que se desea pasar a texto.

    RETURNS
    ---
    str: La palabra en inglés correspondiente al índice del número proporcionado.
    """
    palabras = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    return palabras[numero]


print(switch_it_up(3))  # Salida : Three (Numero a texto)

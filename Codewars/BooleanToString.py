def boolean_to_string(b):
    """Convierte un valor booleano (True o False) en su representación en cadena de texto (String).

    PARAMETERS
    ---
    b (bool): El valor booleano que se desea transformar a texto.

    RETURNS
    ---
    str: Devuelve el resultado de aplicar la función `str()` sobre el booleano, transformándolo en cadena ("True" o "False").
    """
    return str(b)  # método transformación boolean a str (String)


print(boolean_to_string(True))

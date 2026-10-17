def make_upper_case(s):
    """Convierte todos los caracteres de una cadena de texto a mayúsculas.

    PARAMETERS
    ---
    s (str): La cadena de texto que se desea transformar.

    RETURNS
    ---
    str: Devuelve el resultado de aplicar el método upper() sobre la cadena, es decir, el texto completamente en mayúsculas.
    """
    return s.upper()  # método upper


print(make_upper_case("Hola"))  # Salida: HOLA (el texto en mayús)

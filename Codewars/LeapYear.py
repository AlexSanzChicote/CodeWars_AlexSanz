def is_leap_year(year):
    """Determina si un año dado es bisiesto según las reglas del calendario gregoriano.

    PARAMETERS
    ---
    year (int): El año que se desea comprobar.

    RETURNS
    ---
    bool: Devuelve `True` si el año es bisiesto (cumple las condiciones de divisibilidad) o `False` en caso contrario.
    """
    if year % 400 == 0:  # es bisiesto si es divisible entre 400
        return True
    if year % 100 == 0:  # es no bisiesto si es divisible entre 100
        return False
    if year % 4 == 0:  # es bisiesto si es divisible entre 4
        return True
    return False  # si no cumple ninguna de las condiciones anteriores, no es bisiesto


print(is_leap_year(2020))
print(is_leap_year(1900))

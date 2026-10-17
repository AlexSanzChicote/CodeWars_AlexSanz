def evil(n):
    """Determina si un número es 'Evil' (tiene un número par de unos en su representación binaria) o 'Odious' (número impar de unos).

    PARAMETERS
    ---
    n (int): El número entero que se desea evaluar.

    RETURNS
    ---
    str: Devuelve la cadena "It's Evil!" si la cantidad de unos en binario es par, o "It's Odious!" si es impar.
    """
    if bin(n).count('1') % 2 == 0:  # si el numero binario tiene un numero par de unos, es Evil
        return "It's Evil!"
    else:
        return "It's Odious!"


print(evil(3))  # 11

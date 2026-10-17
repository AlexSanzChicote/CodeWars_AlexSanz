def descending_order(num):
    """Reorganiza los dígitos de un número entero en orden descendente para formar el número más grande posible.

    PARAMETERS
    ---
    num (int): El número entero cuyos dígitos se van a reordenar.

    RETURNS
    ---
    int: Devuelve la variable `resultado` con los dígitos reorganizados de mayor a menor.
    """
    resultado = 0
    for i in "9876543210":  # guarda los numeros en orden descendente
        for n in str(num):
            if n == i:
                resultado = resultado * 10 + int(
                    n)  # guarda como un espacio para poder desplazar los numeros y que no se pierdan
    return resultado


print(descending_order(764832895))

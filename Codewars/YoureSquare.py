def is_square(n):
    """Verifica si un número es un cuadrado perfecto (es decir, si tiene una raíz cuadrada exacta).

    PARAMETERS
    ---
    n (int/float): El número que se desea comprobar.

    RETURNS
    ---
    bool: Devuelve `False` si el número es negativo, o un valor booleano (`True` o `False`) comprobando si el cuadrado de su raíz entera es igual a `n`.
    """
    if n < 0:  # anula numeros negativos
        return False

    raiz = int(n ** 0.5)  # raiz cuadrada del numero
    return raiz * raiz == n


print(is_square(4))
print(is_square(5))

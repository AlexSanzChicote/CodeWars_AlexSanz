def square_sum(numbers):
    """Calcula la suma de los cuadrados de todos los números contenidos en una lista o iterable.

    PARAMETERS
    ---
    numbers (list/iterable): Una secuencia o lista de números que se van a elevar al cuadrado y sumar.

    RETURNS
    ---
    int/float: Devuelve el resultado de sumar los cuadrados de cada elemento, obtenido mediante la función `sum()`.
    """
    return sum(n ** 2 for n in numbers)  # suma el cuadrado de los numeros de la lista


print(square_sum([1, 2, 2]))

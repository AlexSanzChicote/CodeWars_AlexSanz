def generate_range(start, stop, step):
    """Genera una lista de números desde un valor inicial hasta un valor final con un incremento determinado.

    PARAMETERS
    ---
    start (int): El número inicial del rango.
    stop (int): El número final del rango (incluido).
    step (int): El incremento o salto entre cada número de la secuencia.

    RETURNS
    ---
    list: Devuelve la lista con la secuencia de números generada mediante `range(start, stop + 1, step)`.
    """
    return list(range(start, stop + 1, step))  # secuencia de números


print(generate_range(1, 10, 1))  # salida: lista del 1 al 10 de 1 en 1

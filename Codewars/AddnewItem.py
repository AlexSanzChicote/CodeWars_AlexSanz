def add_extra(lista_numeros):
    """Crea una nueva lista a partir de la proporcionada y le añade el número 13 al final.

    PARAMETERS
    ---
    lista_numeros (list/iterable): La lista original de números a la que se le añadirá un elemento.

    RETURNS
    ---
    list: Devuelve `lista_nueva`, una copia de la lista original con el número 13 añadido al final.
    """
    lista_nueva = list(lista_numeros)  # copia la lista list() para convertir en lista en caso de que no sea lista
    lista_nueva.append(13)  # añade numero 13
    return lista_nueva  # devuelve la lista con el numero añadido


print(add_extra([1, 2, 3, 4, 5]))  # salida : lista junto el nuevo numero

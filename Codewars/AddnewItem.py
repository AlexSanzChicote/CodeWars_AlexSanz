def add_extra(lista_numeros):
    lista_nueva = list(lista_numeros)
    lista_nueva.append(13) # añade numero 13
    return lista_nueva

print(add_extra([1, 2, 3, 4, 5]))
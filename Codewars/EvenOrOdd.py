def even_or_odd(number):
    text = ""
    if number % 2 == 0: #si el numero es par, devuelve Even
        text = "Even"
    else:
        text = "Odd" #si el numero es impar, devuelve Odd
    return text 

print(even_or_odd(4))
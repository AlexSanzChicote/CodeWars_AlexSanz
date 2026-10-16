def is_square(n):
  if n < 0: #anula numeros negativos
    return False

  raiz = int(n**0.5) #raiz cuadrada del numero
  return raiz * raiz == n 

print(is_square(4))  
print(is_square(5))  
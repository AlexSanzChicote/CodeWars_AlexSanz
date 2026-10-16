def digit_multiplication(s):
  total = 0
  actual = 1
  signo = 1

  for n in f"{s}+":
    if n.isdigit():
      actual *= int(n)  #acumula la multiplicacion de los numeros
    else:
      total += signo * actual  #acumula el total de la multiplicacion
      actual = 1
      signo = 1 if n == "+" else -1 #asigna el signo

  return total

print(digit_multiplication("1+2-3+4"))
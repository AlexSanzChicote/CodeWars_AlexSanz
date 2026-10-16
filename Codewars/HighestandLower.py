def high_and_low(numbers):
  mayor = None
  menor = None
  actual = ""

  
  for i in numbers + " ": 
    if i != " ":
      actual += i #hace que actual sea igual a i
    else:
      if actual:
        num = int(actual) 
         #guarda a mayor y menor
        if mayor is None or num > mayor: 
          mayor = num
        if menor is None or num < menor:
          menor = num
        actual = "" 

  return str(mayor) + "-" + str(menor)  
print(high_and_low("1 2 3 4 5"))
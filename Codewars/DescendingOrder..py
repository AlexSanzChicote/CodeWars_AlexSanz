def descending_order(num):
  resultado = 0
  for i in "9876543210": #guarda los numeros en orden descendente
    for n in str(num):
      if n == i:
        resultado = resultado * 10 + int(n) #guarda como un espacio para poder desplazar los numeros y que no se pierdan
  return resultado

print(descending_order(764832895)) 

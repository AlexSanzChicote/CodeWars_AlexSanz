def evil(n):
    if bin(n).count('1') % 2 == 0: #si el numero binario tiene un numero par de unos, es Evil 
        return "It's Evil!"
    else:
        return "It's Odious!"

print(evil(3))  #11
contador=0
contador1=0
for x in range (10):
    a=int(input("ingrese 10 notas: "))
    if a>=7:
        contador=contador+1
    else:
        contador1=contador1+1
print ("La cantidad de notas mayores o igual a 7 son: ", contador)
print ("La cantidad de notas menores a 7 son: ", contador1)

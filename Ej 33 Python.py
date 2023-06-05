contador=0
contador1=0
for x in range (10):
    a=int(input("ingrese 10 notas: "))
    if a%5==0:
        contador=contador+1
    if a%3==0:
        contador1=contador1+1
print ("Los valores ingresados son multiplos de 5 son: ", contador)
print ("Los valores ingresados son multiplos de 3 son: ", contador1)

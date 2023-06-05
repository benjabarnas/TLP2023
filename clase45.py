continuar="si"
suma=0
while continuar=="si":
    valor=int(input("ingrese el valor entero: "))
    suma=suma+valor
    continuar=(input("Desea cargar otro valor? (ingrese si para continuar)"))
print ("la suma de  los valores ingresados es: ",suma)

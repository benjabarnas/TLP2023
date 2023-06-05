contador = 0
suma = 0
while contador < 10:
    valor = float(input(f"Ingrese el valor {contador+1}: "))
    suma += valor
    contador += 1

promedio = suma / 10
print(f"El promedio de los valores es: {promedio}")
 

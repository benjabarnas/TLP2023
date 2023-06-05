oracion = input("Ingresa una oración: ")

cantidad = 0

for caracter in oracion:
    if caracter == " ":
        cantidad += 1

print("La oración contiene", cantidad, "espacios.")

print("Versión en mayúsculas:", oracion.upper())
print("Versión en minúsculas:", oracion.lower())
print("Versión con la primera letra en mayúscula:", oracion.capitalize())

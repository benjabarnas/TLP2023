print("Ingrese el nombre de una persona en letras minúsculas:")
nombre = input()

if nombre:
    primera_letra = nombre[0]

    if primera_letra == "a" and "e" and "i" and "o" and "u":
        print("El nombre empieza con una vocal.")
    else:
        print("El nombre no empieza con una vocal o no es válido.")

clave=input("ingresa la clave: ")
longitud_clave = len(clave)
while longitud_clave < 10 or longitud_clave > 20:
    print("La clave debe tener entre 10 y 20 caracteres.")
    clave = input("Ingresa una clave válida: ")
    longitud_clave = len(clave)
print("Clave válida:", clave)

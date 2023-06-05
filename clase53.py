frase = input("Ingresa una frase: ")

frase = frase.lower()

contador_vocales = 0

vocales = ['a', 'e', 'i', 'o', 'u']

for letra in frase:
    if letra in vocales:
       contador_vocales += 1
        
print("La frase tiene", contador_vocales, "vocales.")

longitud_oracion = len(frase)

print("Oración en mayúsculas:", frase.upper())
print("Longitud de la oración:", longitud_oracion)

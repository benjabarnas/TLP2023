# Definir una lista vacía
lista_enteros = []

# Cargar valores enteros por teclado y almacenarlos en la lista
numero = int(input("Ingrese un entero (ingrese 0 para finalizar): "))
while numero != 0:
    lista_enteros.append(numero)
    numero = int(input("Ingrese un entero (ingrese 0 para finalizar): "))

# Mostrar el tamaño de la lista
tamanio = len(lista_enteros)
print("Tamaño de la lista:", tamanio)

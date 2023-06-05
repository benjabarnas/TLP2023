# Definir una lista vacía
sueldos = []

# Cargar los sueldos de los operarios
for i in range(5):
    sueldo = float(input("Ingrese el sueldo del operario: "))
    sueldos.append(sueldo)

# Imprimir la lista de sueldos
print("Lista de sueldos:", sueldos)

# Calcular el promedio de los sueldos
promedio = sum(sueldos) / len(sueldos)
print("Promedio de sueldos:", promedio)

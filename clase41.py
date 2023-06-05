# Definimos los contadores para cada turno y la suma de las edades
num_manana = 0
num_tarde = 0
num_noche = 0
suma_manana = 0
suma_tarde = 0
suma_noche = 0

# Pedimos al usuario las edades de los estudiantes del turno mañana
for i in range(5):
    edad = int(input("Ingrese la edad del estudiante del turno mañana: "))
    num_manana =num_manana + 1
    suma_manana =suma_manana + edad

# Pedimos al usuario las edades de los estudiantes del turno tarde
for i in range(6):
    edad = int(input("Ingrese la edad del estudiante del turno tarde: "))
    num_tarde =num_tarde+ 1
    suma_tarde =suma_tarde + edad

# Pedimos al usuario las edades de los estudiantes del turno noche
for i in range(11):
    edad = int(input("Ingrese la edad del estudiante del turno noche: "))
    num_noche =num_noche + 1
    suma_noche =suma_noche + edad

# Calculamos los promedios de edad de cada turno
promedio_manana = suma_manana / num_manana
promedio_tarde = suma_tarde / num_tarde
promedio_noche = suma_noche / num_noche

# Mostramos los promedios de edad de cada turno
print("Promedio de edad del turno mañana:", promedio_manana)
print("Promedio de edad del turno tarde:", promedio_tarde)
print("Promedio de edad del turno noche:", promedio_noche)

# Comparamos los promedios de edad para determinar cuál es mayor
if promedio_manana > promedio_tarde and promedio_manana > promedio_noche:
    print("El turno mañana tiene un promedio de edad mayor.")
else:
    if promedio_tarde > promedio_manana and promedio_tarde > promedio_noche:
       print("El turno tarde tiene un promedio de edad mayor.")
    else:
        print("El turno noche tiene un promedio de edad mayor.")

    

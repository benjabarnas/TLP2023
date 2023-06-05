# Inicializamos las variables contadoras
num_equilateros = 0
num_isosceles = 0
num_escalenos = 0

# Pedimos al usuario la cantidad de triángulos a analizar
n = int(input("Ingrese la cantidad de triángulos que desea analizar: "))

# Iteramos sobre cada triángulo
for i in range(n):
    # Pedimos al usuario los lados del triángulo
    lado1 = float(input("Ingrese el primer lado: "))
    lado2 = float(input("Ingrese el segundo lado: "))
    lado3 = float(input("Ingrese el tercer lado: "))

    # Determinamos el tipo de triángulo
    if lado1 == lado2 == lado3:
        tipo = "equilatero"
        num_equilateros=num_equilateros + 1 
    else:
        if lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            tipo = "isosceles"
            num_isosceles =num_isosceles + 1
        else:
            if lado1!=lado2 or lado1!=lado3 or lado2!=lado3:
                tipo = "escaleno"
                num_escalenos= num_escalenos + 1
           

    # Mostramos al usuario el tipo de triángulo
    print("El triángulo es", tipo)

# Mostramos al usuario la cantidad de triángulos de cada tipo
print("Cantidad de triángulos equilateros:", num_equilateros)
print("Cantidad de triángulos isosceles:", num_isosceles)
print("Cantidad de triángulos escalenos:", num_escalenos)


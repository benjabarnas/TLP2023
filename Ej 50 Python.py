print("Ingrese su correo electrónico:")
email = input()

if "@" in email:
    print("El correo electrónico", email, "es válido.")
else:
    print("El correo electrónico", email, "es inválido. No contiene el símbolo '@'.")

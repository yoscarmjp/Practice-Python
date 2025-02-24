
password = input("Ingresa tu password: ")

if len(password) < 8:
    print("Tu contraseña es muy corta.")
else:
    caracter_para_hashear = "*" 
    cantidad_caracteres = len(password)
    pass_hashed = caracter_para_hashear*cantidad_caracteres
    print(pass_hashed)
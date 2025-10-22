password = input("Ingresa una contraseña: ")

password_isLargue = len(password) > 8
password_isSuper = any(c.isupper() for c in password)
password_ContainNumber = any(c.isdigit() for c in password)


if password_isLargue and password_isSuper and password_ContainNumber:
    print("Contraseña segura.")
else:
    if not password_ContainNumber:
        print("La contraseña le falta mínimo un numero.")
    if not password_isSuper:
        print("La contraseña le falta mínimo una mayuscula.")
    if not password_isLargue:
        print("La contraseña tiene que tener mínimo 8 caracteres")
database = ["yoscar","4858091","mibaby","elimibb"]


while True:
    user = input("Ingresa tu nombre de usuario: ")
    for user_db in database:
        if user_db == user:
            while True:
                password = input("Ingresa tu contraseña: ")
                for password_db in database:
                    if password_db == password:
                        print("Iniciando sesion...")
                        break
                    else:
                        print("Esta contraseña es incorrecta.")
                        break
        else:
            print("Este usuario no fue encontrado en la base de datos.")
            break







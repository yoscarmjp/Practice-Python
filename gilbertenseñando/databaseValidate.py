usuario1 = {
    'username' : 'gilbert',
    'password' : 'onepiece',
    'email' : 'onepiecereviviraenabril@gmail.com'
}

usuario2 = {
    'username' : 'yocal',
    'password' : 'minecraftskywars',
    'email' : 'yocalproekaiwal@gmail.com'
}


while True:
    username = input("\nIngresa tu nombre de usuario: ")
    if username == usuario1['username']:
        while True:
            password = input("\nIngresa tu contraseña: ")
            if len(password) < 8:
                print("\nTu contraseña es muy muy corta.")
            else:
                if password == usuario1['password']:
                    password_hashed = "*"*len(usuario1['password'])
                    print("\nEstas iniciando sesion...")
                    print(f"\nDatos del usuario\n\nUsuario: {usuario1['username']}\nEmail: {usuario1['email']}\nContraseña: {password_hashed}")
                else:
                    print("\nTu contraseña es incorrecta. Intentalo nuevamente.")

    elif username == usuario2['username']:
        while True:
            password = input("\nIngresa tu contraseña: ")
            if len(password) < 8:
                print("\nTu contraseña es muy muy corta.")
            else:
                if password == usuario2['password']:
                    password_hashed = "*"*len(usuario2['password'])
                    print("\nEstas iniciando sesion...")
                    print(f"\nDatos del usuario\n\nUsuario: {usuario2['username']}\nEmail: {usuario2['email']}\nContraseña: {password_hashed}")
                else:
                    print("\nTu contraseña es incorrecta. Intentalo nuevamente.")
    else:
        print("\nEl nombre de usuario no se encuentra en los usuarios registrados.")
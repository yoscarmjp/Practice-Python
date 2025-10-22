
accounts = []
# 2. Revisar balance de cuentas.\n3. Solicitar tarjeta de crédito.\n4. Historial de la cuenta.\n5. Transacciones.

def InitBanking():
    while True:
        try:
            option = int(input("\nBienvenido a MJBank\n\n1. Crear cuenta bancaria\n2. Iniciar sesión\n3. Salir\n\nSelecciona una opción: "))
        except ValueError:
            print("\nDebes ingresar un número")
            continue
        if option == 1:
            CreateAccount()
        elif option == 2:
            LoginAccount()
        elif option == 3:
            print("\nGracias por usar MJBank")
            break
        else:
            print("\nLa opción que elegiste no es válida")  
            continue

def CreateAccount():
    while True:
        name = input("Ingresa tu nombre completo: ")
        if len(name) == 0:
            print("El nombre no puede estar vacío")
            return
        password = input("Crea una contraseña: ")
        if len(password) < 6:
            print("La contraseña debe tener al menos 6 caracteres")
            return
        if not any(char.isdigit() for char in password):
            print("La contraseña debe tener al menos un número")
            return
        
        account = {'name': name, 'password': password, 'balance': 0}
        accounts.append(account)

        print(f"Cuenta creada para {name}")
        InitBanking()

def LoginAccount():
    while True:
        name = input("Ingresa tu nombre completo: ")
        password = input("Ingresa tu contraseña: ")

        for acc in accounts:
            if acc["name"] == name and acc["password"] == password:
                print(f"✅ Bienvenido, {name}. Tu balance es ${acc['balance']:.2f}")
                return
        print("Credenciales incorrectas. Intenta de nuevo.")

InitBanking()
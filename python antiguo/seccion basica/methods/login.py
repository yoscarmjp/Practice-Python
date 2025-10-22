import re

# Array de usuario simulando una base de datos
# Structure: user | password | email
db = ["yoscar", 4858091, "yoscar@gmail.com"]
valid_type_email = "@gmail.com"


def welcome():
    print("""
        Bienvenido a MJPLoginSys+tem
    """)

welcome()
question = int(input("""
Que quieres hacer?
                 
 1 - Registrarte
 2 - Iniciar sesion  

Elige la opcion: """))

def check_password(password):
    patron = r'[^a-zA-Z0-9]'
    if re.search(patron, password):
        return True
    else:
        return False
    
def check_user_email(searching, array):
    if searching in array:
        return True
    else:
        return False


if question == 1:
   while True:
        create_user = input("\nIntroduce tu nombre de usuario: ")

        if check_user_email(create_user, db):
            print("Este usuario ya esta registrado.")
        else:
            while True:
                create_email = input("\nIntroduce tu correo electronico: ")
                if check_user_email(create_email, db):
                    print("Este correo electronico ya esta registrado.")
                else:
                    while True:
                        if create_email.endswith(valid_type_email):    
                            while True:
                                create_pass = input("\nIntroduce tu contraseña segura: ")
                                if check_password(create_pass):
                                    if len(create_pass) < 8:
                                        print("\nTu contraseña es muy corta, tiene que ser superior a 8 caracteres.")
                                    else:
                                        print("\nRegistrando usuario...")
                                        db.extend([create_user, create_pass, create_email])
                                        print(f"\nUsuario {create_user} registrado correctamente")
                                        print(f"\nLa base de datos quedo asi:\n{db}")
                                else:
                                    print("\nEsta contrasena no es segura utiliza caracteres especiales.")
                        else:
                            print("No es una direccion de correo electronico valida.")
                            break

elif question == 2:
    print("\nFuncion aun en desarrollo")
else:
    print(f"""
    {question} no es una opcion valida.
    """)

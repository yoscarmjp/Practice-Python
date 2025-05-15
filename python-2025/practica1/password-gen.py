import random
import string

def password_gen(nivel=12):
    letters = string.ascii_letters
    numbers = string.digits
    characters = string.punctuation

    all_characters = letters + numbers + characters

    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation),
    ]

    password += random.choices(all_characters, k=nivel - 4)
    random.shuffle(password)
    return ''.join(password)

while True:
    select = int(input("¿Que tipo de contraseña deseas generar?" \
    "\n\n 1- Normal (8 Caracteres)\n 2- Básica (6 Caracteres)\n 3- Fuerte (32 Caracteres)" \
    "\n\nEliges la opción: "))
    
    if select == 1:
        print(f"\nTu contraseña normal es: {password_gen(8)}\n")
    elif select == 2:
        print(f"\nTu contraseña básica es: {password_gen(6)}\n")
    elif select == 3:
        print(f"\nTu contraseña fuerte es: {password_gen(32)}\n")
    else:
        print("La opcion seleccionada no es valida.")

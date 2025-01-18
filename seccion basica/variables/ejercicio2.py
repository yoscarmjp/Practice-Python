print("Hola, como te llamas?")
nombre = input("Ingresa tu nombre: ")
print(f"Un gusto conocerte {nombre}, antes de dejarte pasar necesitamos conocer tu edad.")
edad = int(input("Ingresa tu edad: "))

adultos = True

if(edad >= 18):
    print("Perfecto eres mayor de edad.")
else:
    if(adultos == True):
        print("Eres menor de edad pero vienes con adultos perfecto.")
    else:
        print("Eres menor de edad, tienes que venir acompañado de adultos para poder pasar.")
        quit()

print("Tienes alguna reserva?")
reserva = bool(input())

if(reserva == True):
    print("Perfecto, un mesero te acompañará a tu mesa.")
else:
    print("Puedes realizar la reserva, llamando o desde nuestro sitio web.")

print(f"""

    Datos de la persona:
    - Nombre: {nombre}
    - Edad: {edad}
    - Adultos: {adultos}
    - Reserva?: {reserva}

""")
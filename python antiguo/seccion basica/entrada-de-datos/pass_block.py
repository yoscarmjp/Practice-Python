password = input("Ingresa una contraseña: ")

hashed_character = "*"

pass_hashed = hashed_character*len(password)

print(f"\nLa contraseña normal es: {password}")
print("\nLa cantidad de caracteres de la contraseña es:", len(password))
print(f"\nLa contraseña hasheada es: {pass_hashed}")


import random

while True:
    secret_number = random.randint(1, 10)
    user_number = int(input("\nVamos a jugar adivina el numero.\n\nIngresa el numero: "))

    if(secret_number == user_number):
        print(f"\nFelicidades!! El numero correcto era {secret_number}")
    else:
        print(f"\nFallaste! El numero correcto era {secret_number}, puedes jugar de nuevo")
        
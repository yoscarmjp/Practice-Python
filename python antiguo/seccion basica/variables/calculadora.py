while True:
    numero1 = int(input("Ingresa el valor numero 1: "))
    numero2 = int(input("Ingresa el valor numero 2: "))
    operador = input("""
Selecciona que quieres realizar.   
 1. Sumar
 2. Restar
 3. Multiplicar
 4. Dividir
 5. Nada, salir

Eliges la opción: """)

    if operador == '1':
        print("El resultado de la suma es: ", numero1+numero2)
    elif operador == '2':
        print("El resultado de la resta es: ", numero1-numero2)
    elif operador == '3':
        print("El resultado de la multiplicación es: ", numero1*numero2)
    elif operador == '4':

        if numero1 == 0 or numero2 == 0:
            print("No es posible dividirse entre 0")
        else:
            print("El resultado de la divición es: ", numero1/numero2)

    elif operador == '5':
        print("Saliendo de la operación...")
        break
    else:
        print(f"El numero {operador} no es una opción de la calculadora.")

print("Saliendo del la calculadora...")
quit()

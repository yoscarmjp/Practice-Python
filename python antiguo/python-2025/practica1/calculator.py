while True:
    num1 = int(input("\nIngresa el numero 1: "))
    num2 = int(input("\nIngresa el numero 2: "))
    operator = int(input("\nQue operación deseas realizar?\n\n 1- Sumar (+)\n 2- Restar (-)\n 3- Multiplicar (* , x)\n 4- Dividir (/)\n\nEliges la opción: "))

    if(operator == 1):
        result = num1+num2
        print(f"\nEl resultado de la suma es: {result}")
    elif operator == 2:
        result = num1-num2
        print(f"\nEl resultado de la resta es: {result}")
    elif operator == 3:
        result = num1*num2
        print(f"\nEl resultado de la multiplicación es: {result}")
    elif operator == 4:
        if num2 == 0:
            print("No es posible dividir entre 0")
        else:   
            result = num1/num2
            print(f"\nEl resultado de la divición es: {result}")
    else:
        print("\nEsta opción no es valida.")


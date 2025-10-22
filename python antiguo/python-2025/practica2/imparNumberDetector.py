

def listarNumerosParImpar(number):
    for i in range(number):
        result = i % 2
        if result == 0:
            print(f"El numero {i} es un numero impar")
        else:
            print(f"El numero {i} es un numero par")

listarNumerosParImpar(10)
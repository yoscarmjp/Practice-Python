
credit_card = {
    'card_number' : 1234567891011121,
    'card_password' : 4858091,
    'card_owner' : 'Juan',
    'amount' : 16000,
    'card_type' : 'credit'
}
debit_card = {
    'card_number' : 1234567791018978,
    'card_password' : 4858091 ,
    'card_owner' : 'Pedro',
    'amount' : 2000,
    'card_type' : 'debit'
}

print("""
    Bienvenido al cajero automatico.
""")

while True:
    card_number = int(input("introduzca su tarjeta: "))

    if card_number == credit_card['card_number']:
        while True:
            card_pass = int(input("""
                Intruduce la contraseña de tu tarjeta: 
            """))
            if card_pass == credit_card['card_password']:
                withdrawal = int(input("Ingresa el monto a retirar: "))
                while True:
                    if withdrawal > credit_card['amount']:
                        print("""
                            El monto ingresado supera al saldo de la tarjeta.
                        """)
                    elif withdrawal <= 0:
                        print("""
                            El monto ingresado es menor al saldo de la tarjeta.
                        """)
                    else:
                        withdrawal_amount = credit_card['amount'] - withdrawal
                        print(f"""
                            Vas a retirar un monto de {withdrawal}
                            Te queda un restante de {withdrawal_amount}
                        """)
                        while True:
                            confirm = input("""
                                Confirmas tu retiro? (Si / No):
                            """)
                            if confirm == "si":
                                print(f"""
                                    Retirando tus {withdrawal}
                                """)
                                quit()
                            elif confirm == "no":
                                quit()
                            else:
                                print("Esta opcion no existe.")

            else:
                print("La contraseña es inconrrecta.")

    elif card_number == debit_card['card_number']:
        while True:
            card_pass = int(input("""
                Intruduce la contraseña de tu tarjeta: 
            """))

            if card_pass == debit_card['card_password']:
                withdrawal = int(input("Ingresa el monto a retirar: "))

                if withdrawal > debit_card['amount']:
                    print("El monto ingresado supera al saldo de la tarjeta.")
                elif withdrawal <= 0:
                    print("El monto ingresado es menor al saldo de la tarjeta.")
                else:
                    withdrawal_amount = debit_card['amount'] - withdrawal
                    print(f"""
                        Vas a retirar un monto de {withdrawal}
                        Te queda un restante de {withdrawal_amount}
                    """)
                    while True:
                        confirm = input("""
                            Confirmas tu retiro? (Si / No):
                        """)
    
                        if confirm == "si":
                            print(f"""
                                Retirando tus {withdrawal}
                            """)
                            quit()
                        elif confirm == "no":
                            quit()
                        else:
                            print("Esta opcion no existe.")
            else:
                print("La contraseña es inconrrecta.")
    else:
        print("Esta tarjeta no es valida.")
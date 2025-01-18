fecha_actual = 30
fecha_de_pago = 30
sueldo_developers = 10000
developer = {
    'sueldo' : 10000,
    'impuesto' : 0.10,
    'gasto_mensual' : 3500
}

print(f"""
Informacion del usuario:
  Dia de pago > {fecha_de_pago}
  Sueldo > {developer['sueldo']}
  Impuestos de mi sueldo > {developer['impuesto']}
  Gastos Recurrentes > {developer['gasto_mensual']}
""")

if fecha_actual == fecha_de_pago:

    print("Hoy es dia de pago, vamos a proceder con el proceso de tu pago.")
    
    if developer['sueldo'] == sueldo_developers:
        impuesto = developer['impuesto'] * developer['sueldo']
        sueldo_total = developer['sueldo'] - impuesto

        print(f"Tu sueldo total es de {sueldo_total} libre de impuestos.")
        print("Llego la hora de hacer pago a tus gastos del mes")

        sueldo_restante = sueldo_total - developer['gasto_mensual']

        print(f"""
            Tu sueldo restante es de {sueldo_restante}     
        """)

    elif sueldo_developers > developer['sueldo']:
        bono = sueldo_developers - developer['sueldo']

        print(f"Se detecto que tienes un bono en tu sueldo de {bono} usd")

        impuesto = developer['impuesto'] * developer['sueldo']
        sueldo_total = developer['sueldo'] - impuesto

        print(f"Tu sueldo total es de {sueldo_total} libre de impuestos.")
        print("Llego la hora de hacer pago a tus gastos del mes")

        sueldo_restante = sueldo_total - developer['gasto_mensual']

        print(f"""  
            Tu sueldo restante es de {sueldo_restante}
        """)
        
    else:
        print("Hay un problema, el sueldo destinado a los developers no esta completo.")
else:
    print("Lo siento, hoy no es dia de pago.")


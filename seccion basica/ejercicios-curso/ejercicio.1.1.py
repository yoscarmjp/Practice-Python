user_text = input("Ingresa un texto: ")
# template_text = "Hola soy yoscar jajaja lol xd sdasd adasd" # Un texto cualquiera
split_words =  user_text.split() # Dividiendo las palabras

amount_words = len(split_words) # Contando los objetos dividido del array
duration_words = 0.5 # La duracion por cada 2 palabra

total_seconds = duration_words * amount_words 
# Multiplicar el tiempo por palabra por la cantidad de palabras


print(f"\nEl texto contiene {amount_words} palabras.")
if total_seconds >= 60:
    total_minutes = total_seconds / 60
    print(f"\nTardarias {total_seconds}s en decirlo, lo que es igual a {total_minutes}\n")
    if amount_words > 120:
        print("Tremendo testamento te marcaste flaco.")
else:
    print(f"\nTardarias {total_seconds}s en decirlo.\n")

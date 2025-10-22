def polindromo_detector(phrase):
    lower_phrase = phrase.lower()
    invert_phrase = lower_phrase[::-1].replace(" ", "")

    original_phrase = phrase.replace(" ", "")

    if invert_phrase == original_phrase.lower():
        print(f"\nEs un palindromo: {invert_phrase}")
    else:
        print("Esta palabra no es un palindromo.")


while True:
    phrase = input("\nIngresa una frase: ")
    polindromo_detector(phrase)
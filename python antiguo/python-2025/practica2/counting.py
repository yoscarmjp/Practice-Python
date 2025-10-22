
userNumber = int(input("\nIngresa un numero: "))
sum = 0

for i in range(1, userNumber+1):
    if i % 2 == 0:
        print(i)
        sum += i

print(f"\nLa suma de pares es {sum}")
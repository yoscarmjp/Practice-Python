conjunto1 = {8,7,6,5,4,3,2}
conjunto2 = {5,4,3,2}

# Subset
resultado1 = conjunto2.issubset(conjunto1)
resultado2 = conjunto1.issubset(conjunto2)

# SuperSet
resultado3 = conjunto2.issuperset(conjunto1)
resultado4 = conjunto1.issuperset(conjunto2)

# Signo
resultado5 = conjunto2 <= conjunto1
resultado6 = conjunto2 >= conjunto1


print(f"Resultado 1 {resultado1}")
print(f"Resultado 2 {resultado2}")
print(f"Resultado 3 {resultado3}")
print(f"Resultado 4 {resultado4}")
print(f"Resultado 5 {resultado5}")
print(f"Resultado 6 {resultado6}")

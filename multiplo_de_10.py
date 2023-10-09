#Clara Paola Aguilar c. Numero que sea múltiplo de 10


# Entradas
numero = int(input("Ingrese un número: "))

# Proceso
if numero % 10 == 0:
    print(f"El número {numero} sí es múltiplo de 10")
else:
    print(f"El número {numero} no es múltiplo de 10")
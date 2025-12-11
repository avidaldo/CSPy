import add

# Validación de entrada

# Pidiendo permiso
while True:
    num1 = input("introduce un valor: ")
    if num1.replace(",","",1).isnumeric():
        num1 = float(num1)
        break
    print("debes introducir números")
        


# Pidiendo perdón
while True:
    try:
        b = float(input("introduce otro valor: ").replace(",","."))
        break
    except ValueError:
        print("debes introducir números")

print("la suma es: ", add.misuma(num1, b))
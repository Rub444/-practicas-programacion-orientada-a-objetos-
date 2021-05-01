nombre = input("Dime tu nombre: ")
cantidad = int(input("¿Cuántas veces quieres que lo escriba? "))
for i in range(0, cantidad):
    print(nombre)

tabla = int(input("¿Qué tabla de multiplicar quieres? "))
for n in range(1, 11):
    print(tabla, "x", n, "=", tabla*n)


n = int(input("Dime un número "))
print("Los múltiplos de 7 hasta ese número son...")
for i in range(1, n+1):
    if i % 7 == 0:
        print(i)

cantidad = int(input("¿Cuántas veces quieres que te salude? "))
for i in range(0, cantidad):
    print("Hola")
    numero = int(input("Dime el número que quieras ver si es primo: "))
divisores = 0
for i in range(1, numero+1):
    if numero % i == 0:
        divisores += 1
 
if divisores == 2:
    print("Es primo")
else:
    print("No es primo")
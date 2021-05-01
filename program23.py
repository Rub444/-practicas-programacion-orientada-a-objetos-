# Prueba de booleanos
# Ejemplo de la introducción a Python, por Nacho Cabanes
 
n1 = int(input("Dime un número: "))
n2 = int(input("Dime otro número: "))
ambosPares = (n1 % 2 == 0) and (n2 % 2 == 0)
print("Ambos pares?", ambosPares)
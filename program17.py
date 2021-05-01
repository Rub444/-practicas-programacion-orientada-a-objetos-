datos = [10, 20, 30, 40, 50]
print(datos[0])
print(datos[2])
print(datos[4])

datos = []
for n in range(1, 11):
    dato = int(input("Dime el dato "+ str(n) +": "))
    datos.append(dato)
print("Los datos pares son:")
for d in datos:
    if d % 2 == 0:
        print(d)

nombres = ["enero", "febrero", "marzo", "abril", "mayo", "junio",
    "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
mes = int(input("Dime el número de mes (1 a 12): "))
print("Se llama:", nombres[mes-1])
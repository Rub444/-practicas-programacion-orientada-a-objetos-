nombre = input("Dime tu nombre: ")
 
print("Tu inicial es", nombre[0])
print("La cantidad de letras es", len(nombre))
print("La última letra es", nombre[-1])
print("En mayúsculas sería", nombre.upper())
print("Y al revés", nombre[::-1])
 
cantidadDeVocales = 0
for letra in nombre.upper():
    if letra == "A" or letra == "E" or letra == "I" \
            or letra == "O" or letra == "U":
        cantidadDeVocales += 1
 
print("Cantidad de vocales", cantidadDeVocales)
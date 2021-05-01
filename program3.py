numero = int(input("Dígame cuántas palabras tiene la lista: "))

if numero < 1:
    print("¡Imposible!")
else:
    lista = []
    for i in range(numero):
        print("Dígame la palabra", str(i + 1) + ": ", end="")
        palabra = input()
        lista += [palabra]
    print("La lista creada es:", lista)

    buscar = input("Sustituir la palabra: ")
    sustituir = input("por la palabra: ")
    for i in range(len(lista)):
        if lista[i] == buscar:
            lista[i] = sustituir
    print("La lista es ahora:", lista)
def suma(n1, n2, n3):
    return n1+n2+n3
 
print("La suma de 6, 7 y 8 es", suma(6,7,8) )

def cantidadVeces(texto, letra):
    cantidad = 0
    for l in texto:
        if l == letra:
            cantidad += 1
    return cantidad
 
print('Veces que "hasta mañana" contiene una "a":',
    cantidadVeces("hasta mañana", "a") )
    def repetir(letra1, letra2, veces):
    for i in range(0, veces):
        print(letra1, end="")
        print(letra2, end="")
 
repetir("-", "=", 3)
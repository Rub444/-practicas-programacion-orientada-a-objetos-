# Ejemplo de tuplas
# Versión simple
 
nombresDias = ("lunes", "martes", "miercoles", "jueves",
    "viernes", "sabado", "domingo")
numeroDia = int(input("Dime el número de día (1 al 7): "))
print("Su nombre es", nombresDias[ numeroDia-1 ] )
try:
    nombresMeses = ("enero", "febrero", "marzo", "abril",
        "mayo", "junio", "julio", "agosto",
        "septiembre", "octubre", "noviembre", "diciembre")
    numeroMes = int(input("Dime el número de mes (1 al 12): "))
    print("Su nombre es", nombresMeses[ numeroMes-1 ] )
 
except:
    print("Número de mes incorrecto")
    dias = {
    "enero": 31,
    "febrero": 28, 
    "marzo": 31, 
    "abril": 30,
    "mayo": 31, 
    "junio": 30, 
    "julio": 31, 
    "agosto": 31,
    "septiembre" : 30, 
    "octubre": 31, 
    "noviembre": 30, 
    "diciembre": 31
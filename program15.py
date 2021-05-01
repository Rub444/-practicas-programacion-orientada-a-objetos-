suma = int(input("Cuánto es 135+768? "))
while suma != 903:
    suma = int(input("No! Vuelve a intentar... Cuánto es 135+768? "))
print("Perfecto!")

login = input("Dime tu código de acceso: ")
password = input("Dime tu contraseña: ")
while not (login == "1234" and password == "5000"):
    print("Acceso denegado!");
    login = input("Dime tu código de acceso: ")
    password = input("Dime tu contraseña: ")
print("Acceso concedido!");
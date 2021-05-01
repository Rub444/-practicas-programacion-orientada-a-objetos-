lineas = []
for i in range(0, 3):
    frase = input("Dime una frase: ")
    lineas.append(frase + "\n")
 
fichero = open("frases.txt", "w")
fichero.writelines( lineas )
fichero.close()
fichero = open("frases.txt", "a")
fichero.write( input("Dime una frase más: ") + "\n" )
fichero.close()
fichero = open("frases.txt", "r")
lineas = fichero.readlines()
fichero.close()
 
for i in range(0, len(lineas) ):
    print(str(i+1), ":", lineas[i].rstrip())
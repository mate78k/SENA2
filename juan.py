acomulador = 0
contador= 1
while contador <= 10 :
    usuario= input("ingrese el nombre del usuario: ").upper()
    if usuario == "JUAN":
        acomulador +=1
        
    contador += 1
print("La cantidad de veces que se ingreso el nombre JUAN es: ", acomulador)
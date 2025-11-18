acumulador = 0
contador = 1

print(" Bienvenido al juego de apuestas ")

while contador <= 5:
    print("\n--- RONDA", contador, "---")
    apuesta = float(input("Ingrese la cantidad de dinero a apostar: "))

    import random
    
    n1 = random.randint(1, 6)
    n2 = random.randint(1, 6)
    n3 = random.randint(1, 6)

    print("Números obtenidos:", n1, n2, n3)

    
    if n1 == n2 == n3:
        ganancia = apuesta * 3
        print("🎉 ¡Tres iguales! Ganas 3 veces lo apostado.")
    elif n1 == n2 or n2 == n3 or n1 == n3:
        ganancia = apuesta * 1.5
        print("😊 Dos iguales, ganas una vez y media lo apostado.")
    else:
        ganancia = 0
        print("💀 No hay iguales, pierdes todo.")

    acumulador += ganancia
    print("Dinero acumulado hasta ahora: $", acumulador)

    contador += 1

print(" Juego terminado. Dinero total acumulado: $", acumulador)

import random

def obtener_eleccion_jugador():
  
    opciones_validas = ["piedra", "papel", "tijera", "salir"]

    while True:
        eleccion = input("Elige 'piedra', 'papel', 'tijera' o 'salir' para terminar: ").lower()
        if eleccion in opciones_validas:
            return eleccion
        else:
            print("Entrada invalida. Intenta nuevamente.")


def determinar_ganador(jugador, computadora):
  
    if jugador == computadora:
        return "empate"

  
    reglas = {
        "piedra": "tijera",
        "papel": "piedra",
        "tijera": "papel"
    }
    
    if reglas[jugador] == computadora:
        return "jugador"
    else:
        return "computadora"


def juego():
  
    puntaje_jugador = 0
    puntaje_computadora = 0
    opciones = ["piedra", "papel", "tijera"]

    print("Bienvenido al juego de Piedra, Papel o Tijera")

    while True:
        jugador = obtener_eleccion_jugador()

        if jugador == "salir":
            print("Saliendo del juego...")
            break

        computadora = random.choice(opciones)
        print(f"La computadora eligió: {computadora}")

        resultado = determinar_ganador(jugador, computadora)

        if resultado == "jugador":
            puntaje_jugador += 1
            print(" ¡Ganaste la ronda!")
        elif resultado == "computadora":
            puntaje_computadora += 1
            print(" La computadora ganó la ronda.")
        else:
            print(" Empate.")

        print(f"Puntaje → Tú: {puntaje_jugador} | Computadora: {puntaje_computadora}")

    
    print(" PUNTAJE FINAL ")
    print(f"Tú: {puntaje_jugador} | Computadora: {puntaje_computadora}")

    if puntaje_jugador > puntaje_computadora:
        print(" ¡Felicidades! Ganaste el juego.")
    elif puntaje_computadora > puntaje_jugador:
        print(" La computadora ganó el juego. ¡Suerte la próxima!")
    else:
        print(" El juego terminó en empate.")


juego()

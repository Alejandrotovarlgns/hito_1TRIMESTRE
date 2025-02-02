numero_jugador = 0
victorias_usuario = 0
victorias_maquina = 0
# Inicializamos con los datos del juego.
diccionario = {1: "Piedra", 2: "Papel", 3: "Tijera"} 

# Importamos el módulo random para  el número aleatorio.
import random

# El juego continúa hasta que alguno de los dos gane 5 partidas.
while victorias_usuario != 3 and victorias_maquina != 3:
    print(f"----------------------------------------") # Esto es un separador.
    # Generamos la selección de la máquna con un número aleatorio del 1 al 3.
    numero_maquina = random.randint(1,3)
    # Solicitamos al usuario que elija. Se lo volveremos a pedir hasta que elija un número que corresponda con una opción.
    if numero_jugador != 1 and numero_jugador != 2 and numero_jugador != 3:
        # Mostramos el menú al usuario.
        print(f"- ELIGE: 1-Piedra | 2-Papel | 3-Tijera")
        numero_jugador = int(input("Introduce el número correspondiente a la opción que quieras elegir: "))
        if numero_jugador < 1 or numero_jugador > 3:
            print(f"ERROR, introduce un número del 1 al 3 para seleccionar una opción.")
            # Reiniciamos a 0 la variable 'numero_jugador' para comenzar la siguiente ronda.
            numero_jugador = 0
        else:    
            #Mostramos en pantalla lo que  ha elegido el usuario y lo que ha elegido la máquina.
            print(f"Has elegido {diccionario[numero_jugador]}\nLa máquina ha elegido {diccionario[numero_maquina]}")
            #Calculamos quien gana y  lo mostramos.
            if numero_maquina == 1 and numero_jugador == 2:
                print(f"¡Has ganadooooooooo!, punto para ti")
                victorias_usuario = victorias_usuario + 1
                print(f"MARCADOR:\nTú: {victorias_usuario}\nMáquina: {victorias_maquina}")
                numero_jugador = 0
            elif numero_maquina == 1 and numero_jugador == 3:
                print(f"¡Ooooh!, has perdido, punto para la máquina.")
                victorias_maquina = victorias_maquina + 1
                print(f"MARCADOR:\nTú: {victorias_usuario}\nMáquina: {victorias_maquina}")
                numero_jugador = 0
            elif numero_maquina == 2 and numero_jugador == 1:
                print(f"¡Ooooh!, has perdido, punto para la máquina.")
                victorias_maquina = victorias_maquina + 1
                print(f"MARCADOR:\nTú: {victorias_usuario}\nMáquina: {victorias_maquina}")
                numero_jugador = 0
            elif numero_maquina == 2 and numero_jugador == 3:
                print(f"¡Has ganadoooooooooo!, punto para ti")
                victorias_usuario = victorias_usuario + 1
                print(f"MARCADOR:\nTú: {victorias_usuario}\nMáquina: {victorias_maquina}")
                numero_jugador = 0
            elif numero_maquina == 3 and numero_jugador == 1:
                print(f"¡Has ganadoooooooooo!, punto para ti")
                victorias_usuario = victorias_usuario + 1
                print(f"MARCADOR:\nTú: {victorias_usuario}\nMáquina: {victorias_maquina}")
                numero_jugador = 0
            elif numero_maquina == 3 and numero_jugador == 2:
                print(f"¡Ooooooooh!, has perdido, punto para la máquina.")
                victorias_maquina = victorias_maquina + 1
                print(f"MARCADOR:\nTú: {victorias_usuario}\nMáquina: {victorias_maquina}")
                numero_jugador = 0
            else:
                print(f"Vaya, ¡empateeeee!")
                print(f"MARCADOR:\nTú: {victorias_usuario}\nMáquina: {victorias_maquina}")
                numero_jugador = 0
# Mostramos quién ha ganado .
if victorias_usuario == 3:
        print(f"Fin del juego. Enhorabuena, ¡has ganado! :)")
else:
    print(f"Fin del juego. Lo siento, has perdido :(")
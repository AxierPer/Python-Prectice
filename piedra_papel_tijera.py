opciones = ["piedra", "papel", "tijeras"]


def eleccion_ganador(player_uno, name_player_uno, name_player_dos, player_dos):
    if (
        (player_uno == "tijeras" and player_dos == "papel")
        or (player_uno == "piedra" and player_dos == "tijeras")
        or (player_uno == "papel" and player_dos == "piedra")
    ):
        return name_player_uno
    elif player_uno == player_dos:
        resultado = "empate"
        return resultado
    else:
        return name_player_dos


player_uno = input("Escriba el nombre del primer jugador: ")
print(f"Jugador uno: {player_uno}")
player_dos = input("Escriba el nombre del segundo jugador: ")
print(f"Jugador dos: {player_dos}")
turn = False
eleccion_player_uno = ""
eleccion_player_dos = ""
while turn != "":
    if turn == False:
        eleccion_player_uno = input(
            f"{player_uno} elija entre piedra, papel o tijeras: "
        )
        if eleccion_player_uno.lower() in opciones:
            print(f"Su eleccion fue {eleccion_player_uno.lower()}")
            turn = True
        elif eleccion_player_uno.lower() not in opciones:
            print("Eleccion no valida")
    if turn == True:
        eleccion_player_dos = input(
            f"{player_dos} elija entre piedra, papel o tijeras: "
        )
        if eleccion_player_dos.lower() in opciones:
            print(f"Su eleccion fue {eleccion_player_dos.lower()}")
            turn = False
        elif eleccion_player_dos.lower() not in opciones:
            print("Eleccion no valida")

    if (
        eleccion_player_uno.lower() in opciones
        and eleccion_player_dos.lower() in opciones
    ):
        resultado = eleccion_ganador(
            eleccion_player_uno.lower(),
            player_uno,
            player_dos,
            eleccion_player_dos.lower(),
        )
        if resultado != "empate":
            print("El ganador es: ", resultado)
            break
        elif resultado == "empate":
            print(resultado)

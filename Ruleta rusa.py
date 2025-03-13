import random

def ruleta_rusa(jugadores=6, bala_posicion=None):
    if bala_posicion is None:
        bala_posicion = random.randint(1, jugadores)
    
    print("¡Bienvenidos a la Ruleta Rusa!")
    for turno in range(1, jugadores + 1):
        input(f"Jugador {turno}, presiona Enter para apretar el gatillo...")
        if turno == bala_posicion:
            print(f"💥 ¡Jugador {turno} ha sido eliminado! 💥")
            if reiniciar_juego():
                return ruleta_rusa(jugadores)
            else:
                return
        else:
            print(f"🎉 Jugador {turno} sobrevive 🎉")
    else:
        print("Todos los jugadores sobrevivieron. ¡Increíble!")

def reiniciar_juego():
    respuesta = input("¿Quieres jugar de nuevo? (s/n): ").strip().lower()
    return respuesta == 's'

if __name__ == "__main__":
    while True:
        jugadores = int(input("Ingresa el número de jugadores: "))
        ruleta_rusa(jugadores)
        if not reiniciar_juego():
            print("Gracias por jugar. ¡Hasta la próxima!")
            break


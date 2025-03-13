# Ruleta Rusa

Este es un juego de Ruleta Rusa desarrollado en Python. Los jugadores participan en un juego de azar donde uno de ellos será eliminado de forma aleatoria.

## Requisitos
- Python 3.x instalado en tu sistema.

## Cómo jugar
1. Ejecuta el script en la terminal o en un entorno de Python.
2. Ingresa el número de jugadores.
3. Cada jugador presiona Enter para "apretar el gatillo" en su turno.
4. Si la bala coincide con el turno de un jugador, este es eliminado.
5. Después de una eliminación, se preguntará si deseas jugar de nuevo.
6. El juego continuará hasta que los jugadores decidan salir.

## Ejecución
Para ejecutar el programa, usa el siguiente comando en la terminal:
```sh
python Ruleta rusa.py
```

## Lógica del juego
- Se genera aleatoriamente una posición donde se encuentra la bala.
- Cada jugador, en su turno, presiona Enter para ver si sobrevive.
- Si el jugador recibe la bala, es eliminado y se pregunta si desea reiniciar el juego.
- Si todos los jugadores sobreviven, el juego finaliza.

# game.py

import mygame.draw  # Importamos el módulo draw dentro del paquete
from mygame.settings import GAME_NAME

def play_game():
    print(f"Ejecutando {GAME_NAME}...")
    print("Jugando el juego...")
    return "¡Ganaste!"

def main():
    result = play_game()
    # Llamamos a la función del módulo draw
    mygame.draw.draw_game(result)

if __name__ == "__main__":
    main()
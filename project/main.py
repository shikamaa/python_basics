from src.ship_input import get_player_ships
from src.bot_generation import generate_bot_ships
from src.utils import PLAYER_CSV, BOT_CSV, GAME_CSV
from src.gameplay import play_game

def main():
    player_ships = get_player_ships(PLAYER_CSV)
    bot_ships = generate_bot_ships(BOT_CSV)
    game = play_game(player_ships, bot_ships, GAME_CSV)
    print('Game starts...')

if __name__ == '__main__':
    main()

    

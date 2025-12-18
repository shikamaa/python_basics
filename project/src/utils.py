GRID_SIZE = 10
EMPTY_POINT = 0
SHIP_POINT = 1
SHIPS_CFG = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
UNKNOWN = -1
MISS = -2
HIT = 2

#just a comment
PLAYER_CSV = 'data/player_ships.csv'
BOT_CSV = 'data/bot_ships.csv'
GAME_CSV = 'data/game_state.csv'

def is_inside_board(x: int, y: int) -> bool:
    return 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE




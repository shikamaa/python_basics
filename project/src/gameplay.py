import csv
import random
from src.utils import GRID_SIZE, UNKNOWN, HIT, MISS, GAME_CSV

def flatten(grid):
    return [cell for row in grid for cell in row]

def print_board(grid):
    symbols = {
        UNKNOWN: '~',
        MISS: '*',
        HIT: 'X'
    }
    print()
    for col in range(GRID_SIZE):
        if col + 1 < 10:
            print(col + 1, end=' : | ')
        else:
            print(col + 1, end=': | ')
        for row in range(GRID_SIZE):
            print(symbols[grid[col][row]], end=' | ')
        print()
    print('    | ', end='')
    for row in range(1, GRID_SIZE + 1):
        if row < 10:
            print(row, end=' | ')
        else:
            print(row, end='| ')
    print()

def mark_surrounding_miss(grid, ship_cells):
    for x, y in ship_cells:
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                nx, ny = x + dx, y + dy
                if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:
                    if grid[nx][ny] == UNKNOWN:
                        grid[nx][ny] = MISS

def random_move(grid):
    while True:
        x = random.randint(0, GRID_SIZE - 1)
        y = random.randint(0, GRID_SIZE - 1)
        if grid[x][y] == UNKNOWN:
            return x, y

def play_game(player_ships, bot_ships, csv_path=GAME_CSV):
    player_grid = [[UNKNOWN] * GRID_SIZE for _ in range(GRID_SIZE)]
    bot_grid = [[UNKNOWN] * GRID_SIZE for _ in range(GRID_SIZE)]
    
    player_ships_original = [set(ship) for ship in player_ships]
    bot_ships_original = [set(ship) for ship in bot_ships]
    
    with open(csv_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            'turn',
            'player_x', 'player_y', 'player_result',
            'bot_x', 'bot_y', 'bot_result',
            'player_grid', 'bot_grid'
        ])
        
        turn = 1
        while player_ships and bot_ships:
            print('Player board:')
            print(f'You have {len(player_ships)} ships')
            print_board(player_grid)
            print('Bot board:')
            print(f'Bot has {len(bot_ships)} ships')
            print_board(bot_grid)
            
            px, py = map(int, input('Your move (x y): ').split())
            px -= 1
            py -= 1
            
            if bot_grid[px][py] != UNKNOWN:
                print("You already shot here! Try again.")
                continue
            
            player_hit = False
            destroyed_ship_index = None
            
            for i, ship in enumerate(bot_ships):
                if (px, py) in ship:
                    player_hit = True
                    bot_grid[px][py] = HIT
                    ship.remove((px, py))
                    if not ship:
                        destroyed_ship_index = i
                    break
            
            if not player_hit:
                bot_grid[px][py] = MISS
                player_result = 'miss'
            else:
                player_result = 'hit'
                if destroyed_ship_index is not None:
                    mark_surrounding_miss(bot_grid, bot_ships_original[destroyed_ship_index])
                    bot_ships.remove(bot_ships[destroyed_ship_index])
            
            bx, by = random_move(player_grid)
            bot_hit = False
            destroyed_ship_index = None
            
            for i, ship in enumerate(player_ships):
                if (bx, by) in ship:
                    bot_hit = True
                    player_grid[bx][by] = HIT
                    ship.remove((bx, by))
                    if not ship:
                        destroyed_ship_index = i
                    break
            
            if not bot_hit:
                player_grid[bx][by] = MISS
                bot_result = 'miss'
            else:
                bot_result = 'hit'
                if destroyed_ship_index is not None:
                    mark_surrounding_miss(player_grid, player_ships_original[destroyed_ship_index])
                    player_ships.remove(player_ships[destroyed_ship_index])
            
            writer.writerow([
                turn,
                px, py, player_result,
                bx, by, bot_result,
                flatten(player_grid),
                flatten(bot_grid)
            ])
            
            turn += 1
        
        print('Player board:')
        print_board(player_grid)
        print('Bot board:')
        print_board(bot_grid)
        print('You win!' if not bot_ships else 'Bot wins!')
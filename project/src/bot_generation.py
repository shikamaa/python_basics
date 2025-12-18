import random
from src.utils import GRID_SIZE, EMPTY_POINT, SHIP_POINT, SHIPS_CFG
from src.ship_input import is_touching, is_valid_ship
import csv

def generate_bot_ships(path) -> list:
    grid = [[EMPTY_POINT] * GRID_SIZE for _ in range(GRID_SIZE)]
    ships = []

    for size in SHIPS_CFG:
        while True:
            x = random.randint(0, GRID_SIZE - 1)
            y = random.randint(0, GRID_SIZE - 1)
            direction = random.choice(["Horizontal", "Vertical"])

            points = []
            for i in range(size):
                nx = x + i if direction == "Vertical" else x
                ny = y + i if direction == "Horizontal" else y

                if not (0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE):
                    points = []
                    break
                if grid[nx][ny] == SHIP_POINT or is_touching(grid, nx, ny):
                    points = []
                    break

                points.append((nx, ny))

            if not points or not is_valid_ship(points):
                continue

            for px, py in points:
                grid[px][py] = SHIP_POINT

            ships.append(points)
            break

    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ship_id", "x", "y"])
        for sid, ship in enumerate(ships):
            for x, y in ship:
                writer.writerow([sid, x, y])

    return ships
    
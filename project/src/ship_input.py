import csv
from src.utils import GRID_SIZE, EMPTY_POINT, SHIP_POINT, SHIPS_CFG, is_inside_board

TEST_SHIPS = [
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(2, 5), (3, 5), (4, 5)],
    [(6, 1), (6, 2), (6, 3)],
    [(9, 7), (9, 8)],
    [(4, 0), (5, 0)],
    [(7, 9), (8, 9)],
    [(2, 2)],
    [(5, 5)],
    [(8, 3)],
    [(1, 9)],
]


def print_field(grid):
    print()
    for x in range(GRID_SIZE):
        print(f"{x+1:2} | ", end="")
        for y in range(GRID_SIZE):
            print(grid[x][y], end=" | ")
        print()
    print("    " + "---" * GRID_SIZE)


def is_touching(grid, x, y):
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            nx, ny = x + dx, y + dy
            if is_inside_board(nx, ny) and grid[nx][ny] == SHIP_POINT:
                return True
    return False


def is_valid_ship(points):
    if len(points) == 1:
        return True

    xs = [p[0] for p in points]
    ys = [p[1] for p in points]

    return (
        len(set(xs)) == 1 and sorted(ys) == list(range(min(ys), max(ys) + 1))
    ) or (
        len(set(ys)) == 1 and sorted(xs) == list(range(min(xs), max(xs) + 1))
    )


def get_point():
    while True:
        try:
            x, y = map(int, input("Enter coordinates (x y): ").split())
            x -= 1
            y -= 1
            if is_inside_board(x, y):
                return x, y
            print("Outside board")
        except ValueError:
            print("Wrong input")


def fill_grid():
    grid = [[EMPTY_POINT] * GRID_SIZE for _ in range(GRID_SIZE)]
    ships = []

    print_field(grid)

    for size in SHIPS_CFG:
        while True:
            print(f"Deploy ship of size {size}")
            points = []

            for _ in range(size):
                x, y = get_point()
                if grid[x][y] == SHIP_POINT or is_touching(grid, x, y):
                    points = []
                    break
                points.append((x, y))

            if len(points) != size or not is_valid_ship(points):
                continue

            for x, y in points:
                grid[x][y] = SHIP_POINT

            ships.append(points)
            print_field(grid)
            break

    return ships


def save_ships(path, ships):
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ship_id", "x", "y"])
        for sid, ship in enumerate(ships):
            for x, y in ship:
                writer.writerow([sid, x, y])


def load_ships(path):
    ships = {}
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            sid = int(row["ship_id"])
            ships.setdefault(sid, []).append((int(row["x"]), int(row["y"])))
    return list(ships.values())


def get_player_ships(csv_path):
    while True:
        choice = input("Template grid (1) or custom (0): ").strip()
        if choice == "1":
            ships = TEST_SHIPS
            break
        if choice == "0":
            ships = fill_grid()
            break
        print("Enter 0 or 1")

    save_ships(csv_path, ships)
    return ships

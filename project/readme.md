# Battleship Game

Console Battleship game. You vs Bot.

## How to Play

### Place Ships
Format: `x1 y1 x2 y2`
```
Enter ship coordinates: 1 1 1 4
```
This makes a 4-cell vertical ship.

### Shoot
Format: `x y`
```
Your move: 5 3
```

### Symbols
- `~` = Not shot yet
- `*` = Miss
- `X` = Hit

## Rules

Ships must be:
1. Straight (no diagonals)
2. Correct size (1, 2, 3, or 4 cells)
3. Inside the board
4. Not touching each other

## Game

Two boards show:
- Your ships (bot shoots here)
- Bot ships (you shoot here)

When ship destroyed, cells around it auto-marked as miss.

First to sink all enemy ships wins.
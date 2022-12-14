# Map is a matrix of 12x12
WORLD_MAP = [
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['X', ' ', 'X', ' ', 'X', ' ', ' ', ' ', ' ', ' ', ' ', 'X'],
    ['X', ' ', 'X', ' ', 'X', ' ', 'X', ' ', 'X', 'X', 'X', 'X'],
    ['X', ' ', 'X', ' ', 'X', ' ', ' ', ' ', ' ', ' ', ' ', 'X'],
    ['X', ' ', ' ', ' ', 'X', 'X', 'X', 'X', ' ', 'X', 'X', 'X'],
    ['X', ' ', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X'],
    ['X', ' ', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', ' ', 'X'],
    ['X', ' ', ' ', ' ', 'X', ' ', 'X', ' ', 'C', 'X', ' ', 'X'],
    ['X', ' ', 'X', ' ', 'X', ' ', 'X', ' ', ' ', 'X', ' ', 'X'],
    ['X', ' ', 'X', ' ', 'X', ' ', 'X', ' ', 'X', 'X', ' ', 'X'],
    ['X', ' ', 'X', ' ', 'X', ' ', ' ', ' ', ' ', ' ', ' ', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
]

FREE_COORDINATES = []
for i in range(len(WORLD_MAP)):
    for j in range(len(WORLD_MAP[i])):
        if WORLD_MAP[i][j] != 'X' and WORLD_MAP[i][j] != 'C':
            FREE_COORDINATES.append((i, j))

WALL_COORDINATES = []
for i in range(len(WORLD_MAP)):
    for j in range(len(WORLD_MAP[i])):
        if WORLD_MAP[i][j] == 'X':
            WALL_COORDINATES.append((i, j))

CHEST_COORDINATES = []
for i in range(len(WORLD_MAP)):
    for j in range(len(WORLD_MAP[i])):
        if WORLD_MAP[i][j] == 'C':
            CHEST_COORDINATES.append((i, j))

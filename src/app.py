import os
import random


## create a grid for the mines
def grid():
    width = int(8)
    height = int(8)
    grid = []
    i = int(0)
    for i in range(width):
        grid.append(0)
    for i in range(height):
        print(grid)

    # for x, y in enumerate(grid):
    #     x = random.randint(0, 8)
    #     y = random.randint(0, 8)
    #     grid[y][x] = "X"


box = grid()

coordinates = [(i, j) for j in range(8) for i in range(8)]


print(coordinates)


## one random bomb

# def one_bomb():
#     box = grid()
#     x = random.randint(0, 8)
#     y = random.randint(0, 8)
#     box[y][x] = 'X'

# one_bomb()

# items = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for index, item in enumerate(items):
#     if not (item % 2):
#         items[index] = None

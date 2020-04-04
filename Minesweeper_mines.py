#
# for setting up the mines, the numbers around the mines,
# and to update each list element for the mines it touches
#

import random as r
field = [[0 for i in range(10)] for j in range(10)]
num_mines = 15


# used to place the mines
def mines():
    global field

    i = 0
    while i != num_mines:
        x = r.randint(0, 9)
        y = r.randint(0, 9)

        # place mine
        if field[x][y] != 9:
            field[x][y] = 9
            i += 1


# increment numbers around mines
def increment_neighbors():
    global field

    for row in range(len(field)):
        for col in range(len(field[row])):
            # mine
            if field[row][col] == 9:

                # To the right
                if col + 1 < len(field) and field[row][col + 1] != 9:
                    field[row][col + 1] += 1

                # Below the mine
                if row + 1 < len(field) and field[row + 1][col] != 9:
                    field[row + 1][col] += 1

                # Above the mine
                if row - 1 >= 0 and field[row - 1][col] != 9:
                    field[row - 1][col] += 1

                # To the left
                if col - 1 >= 0 and field[row][col - 1] != 9:
                    field[row][col - 1] += 1

                # Down right
                if row + 1 < len(field) and col + 1 < len(field[row]) and field[row + 1][col + 1] != 9:
                    field[row + 1][col + 1] += 1

                # Up right
                if row - 1 >= 0 and col + 1 < len(field[row]) and field[row - 1][col + 1] != 9:
                    field[row - 1][col + 1] += 1

                # Up left
                if row - 1 >= 0 and col - 1 >= 0 and field[row - 1][col - 1] != 9:
                    field[row - 1][col - 1] += 1

                # Down left
                if row + 1 < len(field) and col - 1 >= 0 and field[row + 1][col - 1] != 9:
                    field[row + 1][col - 1] += 1


# adds mines and the numbers to list: fields
def create_map():
    mines()
    increment_neighbors()


create_map()
for i in range(len(field)):
    print(field[i])

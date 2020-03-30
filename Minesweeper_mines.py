#
# for setting up the mines, the numbers around the mines,
# and to be able to recursively uncover the buttons
#

import random as r
field = [[0 for i in range(10)] for j in range(10)]


def mines():
    global field

    i = 0
    while i != 20:
        x = r.randint(0, 9)
        y = r.randint(0, 9)

        # place mine
        if field[x][y] != 9:
            field[x][y] = 9
            i += 1


#FIXME: python <- java
def increment_neighbors():
    for row in field.len:
        for col in field[row].len:

            # To the right
            if field[row + 1] < field.len and field[row][col + 1] != 9:
                map[row][col + 1].incrementContents()

            # Below the mine
            if row + 1 < map.length and map[row + 1][col].getContents() != 9:
                map[row + 1][col].incrementContents()

            # Above the mine
            if row - 1 >= 0 and map[row - 1][col].getContents() != 9:
                map[row - 1][col].incrementContents()

            # To the left
            if col - 1 >= 0 and map[row][col - 1].getContents() != 9:
                map[row][col - 1].incrementContents()

            # Down right
            if row + 1 < map.length and col + 1 < map[row].length and map[row + 1][col + 1].getContents() != 9:
                map[row + 1][col + 1].incrementContents()

            # Up right
            if row - 1 >= 0 and col + 1 < map[row].length and map[row - 1][col + 1].getContents() != 9:
                map[row - 1][col + 1].incrementContents()

            # Up left
            if row - 1 >= 0 and col - 1 >= 0 and map[row - 1][col - 1].getContents() != 9:
                map[row - 1][col - 1].incrementContents()

            # Down left
            if row + 1 < map.length and col - 1 >= 0 and map[row + 1][col - 1].getContents() != 9:
                map[row + 1][col - 1].incrementContents()


mines()
print(field)

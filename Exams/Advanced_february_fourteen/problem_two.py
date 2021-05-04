field_size = int(input())
field = [[x for x in input().split()] for _ in range(field_size)]

pos = []
path_taken = []

total_coins = 0
is_dead = False

for i in range(field_size):
    for j in range(field_size):
        if field[i][j] == "P":
            pos.extend((i, j))


def get_item(position, coins, is_dead=is_dead):
    if field[position[0]][position[1]] == "X" or position[1] > field_size-1 or position[1] < 0 or position[0] < 0 \
            or position[0] > field_size-1:

        coins = int(coins // 2)
        is_dead = True
    else:
        coins += int(field[position[0]][position[1]])
    return coins, is_dead


while is_dead == False and total_coins < 100:
    command = input()

    if command == "up":
        pos = [pos[0] - 1, pos[1]]

        total_coins, is_dead = get_item(pos, total_coins)
        if is_dead:
            break
        else:
            path_taken.append(pos)

    if command == "down":
        pos = [pos[0] + 1, pos[1]]

        total_coins, is_dead = get_item(pos, total_coins)
        if is_dead:
            break
        else:
            path_taken.append(pos)

    if command == "left":
        pos = [pos[0], pos[1] - 1]

        total_coins, is_dead = get_item(pos, total_coins)
        if is_dead:
            break
        else:
            path_taken.append(pos)

    if command == "right":
        pos = [pos[0], pos[1] + 1]

        total_coins, is_dead = get_item(pos, total_coins)
        if is_dead:
            break
        else:
            path_taken.append(pos)
    if total_coins >= 100:
        print(f"You won! You've collected {total_coins} coins.")
        print(f"Your path:")
        print(*path_taken, sep="\n")

if is_dead:
    print(f"Game over! You've collected {total_coins} coins.")
    print(f"Your path: ")
    print(*path_taken, sep="\n")

"""
inputs:
5
1 X 7 9 11
X 14 46 62 0
15 33 21 95 X
P 14 3 4 18
9 20 33 X 0
right
right
up
up
left
down



8
13 18 9 7 24 41 52 11
54 21 19 X 6 4 75 6
76 5 7 1 76 27 2 37
92 3 25 37 52 X 56 72
15 X 1 45 45 X 7 63
1 63 P 2 X 43 5 1
48 19 35 20 100 27 42 80
73 88 78 33 37 52 X 22
up
left
"""
import math

player_names = input().split(", ")
dartboard = [[x for x in input().split(" ")] for _ in range(7)]

p1_points = 501
p2_points = 501
round = 0


def get_points(coordinates):
    total_score = 0

    if dartboard[coordinates[0]][coordinates[1]] == "D" or dartboard[coordinates[0]][coordinates[1]] == "T":
        for item in range(7):
            if dartboard[coordinates[0]][item].isdigit():
                total_score += int(dartboard[coordinates[0]][item])
            else:
                continue
        for row in range(7):
            if dartboard[row][coordinates[1]].isdigit():
                total_score += int(dartboard[row][coordinates[1]])
            else:
                continue
        if dartboard[coordinates[0]][coordinates[1]] == "D":
            total_score *= 2
        elif dartboard[coordinates[0]][coordinates[1]] == "T":
            total_score *= 3

    elif dartboard[coordinates[0]][coordinates[1]] == "B":
        total_score = 1000

    else:
        total_score += int(dartboard[coordinates[0]][coordinates[1]])

    return total_score

while p1_points > 0 and p2_points > 0:
    miss = False

    round += 1
    trow = input()
    trow = list(trow[1:-1].split(", "))
    trow = [int(x) for x in trow]

    for x in trow:
        if x >= 8:
            miss = True

    if round % 2 == 0:
        if miss:
            continue
        else:
            p2_points -= get_points(trow)
    else:
        if miss:
            continue
        else:
            p1_points -= get_points(trow)

if p1_points <= 0:
    print(f"{player_names[0]} won the game with {math.ceil(round/2)} throws!")
elif p2_points <= 0:
    print(f"{player_names[1]} won the game with {math.ceil(round / 2)} throws!")

"""
example input

Ivan, Peter
12 21 18 4 20 7 11
9 D D D D D 10
15 D T T T D 3
2 D T B T D 19
17 D T T T D 6
22 D D D D D 14
5 8 23 13 16 1 24
(3, 4)

"""
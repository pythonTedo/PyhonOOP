firework_effects = input().split(", ")
explosive_power = input().split(", ")

firework_effects = [int(i) for i in firework_effects if int(i) > 0]
explosive_power = [int(i) for i in explosive_power if int(i) > 0]

fire = {"Palm Fireworks": 0, "Willow Fireworks": 0, "Crossette Fireworks": 0}

temp_num = 0
while firework_effects and explosive_power:

    firework_effects = [int(i) for i in firework_effects if int(i) > 0]
    explosive_power = [int(i) for i in explosive_power if int(i) > 0]

    if not firework_effects and explosive_power:
        continue

    temp_num = firework_effects[0] + explosive_power[-1]

    if temp_num % 3 == 0 and temp_num % 5 == 0:
        fire['Crossette Fireworks'] += 1
        firework_effects.pop(0)
        explosive_power.pop(-1)

    elif temp_num % 3 == 0 and temp_num % 5 != 0:
        fire['Palm Firework'] += 1
        firework_effects.pop(0)
        explosive_power.pop(-1)

    elif temp_num % 3 != 0 and temp_num % 5 == 0:
        fire['Willow Fireworks'] += 1
        firework_effects.pop(0)
        explosive_power.pop(-1)

    else:
        firework_effects[0] -= 1
        firework_effects.append(firework_effects.pop(0))

if fire["Palm Fireworks"] >= 3 and fire["Willow Fireworks"] >= 3 and fire["Crossette Fireworks"] >= 3:
    print(f"Congrats! You made the perfect firework show!")
    for key, value in fire.items():
        print(f"{key}: {value}")

else:
    print("Sorry. You can’t make the perfect firework show.")
    if len(firework_effects) > 0:
        print(f"Firework Effects left: {', '.join([str(i) for i in firework_effects])}")
    if len(explosive_power) > 0:
        print(f"Explosive Power left: {', '.join([str(i) for i in explosive_power])}")
    for key, value in fire.items():
        print(f"{key}: {value}")


"""
inputs:
5, 6, 4, 16, 11, 5, 30, 2, 3, 27
1, 13, 5, 3, -7, 32, 19, 3, 5, 7, 22


-15, -8, 0, -16, 0, -22
10, 5
"""
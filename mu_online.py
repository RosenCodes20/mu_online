initial_health = 100
initial_bonus = 0
rooms = input().split("|")

for lenght in range(len(rooms)):
    command, num = [int(x) if x[-1].isdigit() else x for x in rooms[lenght].split()]

    if command == "potion":
        if initial_health + num > 100:
            num = 100 - initial_health
        initial_health += num
        print(f"You healed for {num} hp.")
        print(f"Current health: {initial_health} hp.")
        continue
    if command == "chest":
        initial_bonus += num
        print(f"You found {num} bitcoins.")
        continue

    initial_health -= num

    if initial_health > 0:
        print(f"You slayed {command}.")
        continue
    else:
        print(f"You died! Killed by {command}.")
        print(f"Best room: {lenght + 1}")
        break
else:
    print("You've made it!")
    print(f"Bitcoins: {initial_bonus}")
    print(f"Health: {initial_health}")

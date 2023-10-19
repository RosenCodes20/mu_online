rooms = input().split("|")
best_room = 0
is_killed = False
current_health = 100
bitcoins = 0
for room in rooms:
    best_room += 1
    current_room, number = room.split()

    if current_room == "potion":
        temp_health = current_health
        current_health += int(number)

        if current_health > 100:
            current_health = 100
        number = temp_health - current_health
        print(f"You healed for {abs(number)} hp.")
        print(f"Current health: {current_health} hp.")
    elif current_room == "chest":
        bitcoins += int(number)
        print(f"You found {number} bitcoins.")

    else:
        current_health -= int(number)
        if current_health > 0:
            print(f"You slayed {current_room}.")
        else:
            print(f"You died! Killed by {current_room}.")
            print(f"Best room: {best_room}")
            break
else:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {current_health}")

#initial_health = 100
#initial_bonus = 0
#rooms = input().split("|")

#for lenght in range(len(rooms)):
    #command, num = [int(x) if x[-1].isdigit() else x for x in rooms[lenght].split()]

    #if command == "potion":
       # if initial_health + num > 100:
           # num = 100 - initial_health
        #initial_health += num
        #print(f"You healed for {num} hp.")
        #print(f"Current health: {initial_health} hp.")
        #continue
    #if command == "chest":
        #initial_bonus += num
        #print(f"You found {num} bitcoins.")
        #continue

    ##initial_health -= num

    ##if initial_health > 0:
        ##print(f"You slayed {command}.")
        ##continue
    ##else:
        #print(f"You died! Killed by {command}.")
       #print(f"Best room: {lenght + 1}")
        #break
#else:
    #print("You've made it!")
    #print(f"Bitcoins: {initial_bonus}")
    #print(f"Health: {initial_health}")

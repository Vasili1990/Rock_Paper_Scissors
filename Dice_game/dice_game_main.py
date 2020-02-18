def dice_roll():
    import random
    x = random.randint(1, 6)
    return x

numoftr = int(input("Numer of tries: "))

Player = dice_roll()
Computer = dice_roll()

i = 0
while i < numoftr:
    Player = dice_roll()
    Computer = dice_roll()
    if Player > Computer:
        print("You won")
        print("Player: " + str(Player) + " / " + "Computer: " + str(Computer))
    elif Player == Computer:
        print("Draw")
        print("Player: " + str(Player) + " / " + "Computer: " + str(Computer))
    elif Player < Computer:
        print("You lost")
        print("Player: " + str(Player) + " / " + "Computer: " + str(Computer))
    else:
        print("Try again")
    i = i +1
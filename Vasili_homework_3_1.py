x = input("Rock, Paper or Scissors (r/p/s) : ")

import random

versions = ["r", "p", "s"]

comp = random.choice(versions)

result = str(x) + str(comp)


if (result == "rr" or result == "pp" or result == "ss"):
     print("Player: " + x + " / " "Computer: " + comp +" / " + "Draw" )
elif (result == "rs" or result == "sp" or result == "pr"):
     print("Player: " + x + " / " "Computer: " + comp +" / " + "Player Won" )
elif (result == "rp" or result == "sr" or result == "ps"):
     print("Player: " + x + " / " "Computer: " + comp +" / " + "Computer Won" )
else:
    print("try again")
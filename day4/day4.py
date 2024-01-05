import random

choice = input("Heads or Tails? Type 1 for heads and 2 for Tails ")

heads_tails = random.randint(1, 2)

if heads_tails == 1: 
    print("Heads")
    if choice == 1 & heads_tails == 1:
        print("You got it!")
    else:
        print("Sorry")

elif heads_tails == 2:
    print("Tails")
    if choice == 2 & heads_tails == 2:
        print("You got it!")
    else:
        print("Sorry")



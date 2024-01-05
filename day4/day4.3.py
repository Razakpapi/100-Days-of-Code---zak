import random

rock = 'O'

paper = '|||'

scissors = 'X'


game_combo = [rock, paper, scissors]



random_results = random.choice(game_combo)

choices = int(input('Pick between Rock, Paper and Scissors. Type "0" for Rock, "1" for Paper and "2" for Scissors '))
if choices >= 3 or choices < 0:
    print("You typed an invalid number. You lose!")
else:

    print(game_combo[choices])

    computer_choice = random.randint(0, 2)


    print(f"Computer chose:")

    print(game_combo[computer_choice])

    if choices == 0 and computer_choice == 2:
        print("You win")

    elif computer_choice > choices:
        print("You Lose")
    elif computer_choice == choices:
        print("Its a draw")
    elif computer_choice == 0 and choices == 2:
        print("You lose")
    elif computer_choice == 0 and choices == 1:
        print("You win")



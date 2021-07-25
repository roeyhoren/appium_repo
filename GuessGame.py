def GuessGame():
    return ()
import random

difficulty = random.randint(1,20)

player_selected = input(" please select a number between 1 to 20\n " " Please note you only have 1 shut ")
print(player_selected)

generated_number = int(difficulty)
selected_number = int(player_selected)


if generated_number != selected_number:
   print("Incorrect, Game selected", difficulty, "and you selected ", player_selected, "try again!")
else:
    print("You have wom!!!, the numbers are equal")





def CurrencyRouletteGame():
    return ()
from currency_converter import CurrencyConverter
c = CurrencyConverter()

ret = c.convert(1, 'USD', 'ILS')

int_difficulty = input("please select difficulty from 1 to 5\n")
difficulty = int_difficulty
print("you have selected difficulty: " ,difficulty)

import random

random_dollar_number = random.randint(1,100)
print("how much is", random_dollar_number, "$ in Isreali shekel")
print(ret)
t = random_dollar_number * ret
print(t)

guess = input("Enter your guess:\n")
player_guess = int(guess)
print(player_guess)
low_diff_range = 5 - int(difficulty)
max_diff_range = 5 + int(difficulty)

interval = (t - (low_diff_range), t + (5 - max_diff_range))
if interval[0] < player_guess < interval[1]:
    print("you won")
else:
    print("you loss")


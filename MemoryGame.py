def MemoryGame():
    return ()
import random
import time
difficulty = [random.randrange(1, 101, 1) for i in range(5)]
d = difficulty
# printing result
print("Random number list is : " + str(difficulty))

time.sleep(0.7)

def get_list_from_user():
    user_lst_input = input("please enter your list:\n")
    usr_list = []
    for string in user_lst_input.split(" "):
        usr_list.append(int(string))
    return usr_list
if get_list_from_user() == difficulty:
    print("you won")
else:
    print("you loss")



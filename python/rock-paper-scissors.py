import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


user_input = int(input("what do you choose? type 0 for rock, 1 for paper and 2 for scissors. \n"))

game_image = [rock, paper, scissors]
computer_choose = random.randint(0, 2)




if user_input >= 3 or user_input < 0:
    print("You typed an invalid number, You lose....")
else:
    print(game_image[user_input])
    print(f"Computer choose {game_image[computer_choose]}")
    if user_input == 0 and computer_choose == 1:
        print("You lose")
    elif user_input == 1 and computer_choose == 2:
        print("You lose")
    elif user_input == 2 and computer_choose == 0:
        print("You lose")
    elif user_input == computer_choose:
        print("It's draw")
    else:
        print("You win")

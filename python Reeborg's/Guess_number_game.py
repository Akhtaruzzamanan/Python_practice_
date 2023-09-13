import random # import random libary
random_number = random.randint(1, 100)
print("Welcome to the number guessing game")
print(random_number)
attempts = 0
game_over = False

# def guess_number_function(level):
#     if lavel == "easy":
#         print("you will have 10 attempts of chance")
#         if attempts == 10:
#             print("Your game is over")
#     else:
#         print("you will have 5 attempts of chance")
#         if attempts == 5:
#             print("Your game is over")

while not game_over:
    attempts += 1
#     game_level = input("What level you want to play? 'easy' or 'hard' ").lower()
    guess_number = int(input("Guess the number (between 1 and 100) "))
    
    print(guess_number)
#     if game_level == "easy":
#         print("you will have 10 attempts of chance")
#         if attempts == 10:
#             print("Your game is over")
#             break
#     else:
#         print("you will have 5 attempts of chance")
#         if attempts == 5:
#             print("Your game is over")
#             break

    if guess_number == random_number:
        print("Yes, your guess is correct")
        break
    elif guess_number > random_number:
        print("Incorrect! Please try to guess a smaller number.")
    else:
        print("Incorrect! Please try to guess a larger number.")
        
#     guess_number_function(game_level)
print(f"You tried {attempts} times to find the correct number")

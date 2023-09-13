import random
print("*********** Welcome to hangman game *******")
word_list = ['apple', 'banana', 'goava', 'mango']

chosen_word = random.choice(word_list)

print(chosen_word)


display = []
for _ in range(len(chosen_word)):
    display += "_"

end_of_games = False
while not end_of_games:
    
    guess = input("Guess a letter: ").lower()
    print(guess)

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
        
    print(display)
    
    if "_" not in display:
        end_of_games = True
        print("You win.")

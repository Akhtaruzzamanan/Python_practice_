from game_data import data
from art import logo, vs
import random

def formate_data(account):
    """Takes the account data and returns the printable formate"""
    account_name = account['name']
    account_description = account['description']
    account_country = account['country']
    return f"{account_name} a {account_description} from {account_country}"

#Use if statement to cheack if user is correct
def cheack_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and returns if they got it right"""
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'

# Display art
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)
# print(f"{account_b['follower_count']}")
while game_should_continue:
    #import random 
    #Making account at position B become next account a position A
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)
    #format data from database 
    print(f"Compare A: {formate_data(account=account_a)}")
    print(vs)
    print(f"Against B: {formate_data(account=account_b)}")

    #Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    ##Get flower count of each account
    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']
    is_correct = cheack_answer(guess=guess, a_followers=a_follower_count, b_followers=b_follower_count)

    #Give user feedback on their guess
    if is_correct:
        #score kipping
        score += 1
        print(f"You're right! Your current score: {score}")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Your final score: {score}")
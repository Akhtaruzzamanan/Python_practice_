import random

number = random.randint(1, 1000)
attempts = 0
low = 1 #automatic program need this number
high = 1000 #automatic program need this number

while True:
    #input_number = input("Guess the number (between 1 and 1000): ") #it was manual guess number part
    print("Guess the number (between 1 and 1000): ")
    #input_number = int(input_number) #it was manual guess number part
    input_number = (low + high) // 2 #Only integer division
    print("My guess is", input_number)
    attempts += 1
    
    if input_number == number:
        print("Yes, your guess is correct!")
        break
    elif input_number > number:
        print("Incorrect! Please try to guess a smaller number.")
        high = input_number - 1 #It's automatic program
    else:
        print("Incorrect! Please try to guess a larger number")
        low = input_number + 1 #It's automatic program 
        
print("You tried", attempts, "times to find the correct number")
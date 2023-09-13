#Banker Roulette - Who will pay the bill
import random
names_string = input("Give me everybody's name, seperated by a comma. ")

names = names_string.split(", ")

# person = random.randint(0, len(names)-1)		#||
# who = names[person]							#||
                                                #|| there are different code but same work
who = random.choice(names)						#||
print(f"{who} is going to meal today !")
# name = input("What is your name? \n")
# name.lower()
# 
# if name.startswith("mr"):
#     print("Hello sir, how are you? ")
# elif name.startswith("mrs") or name.startswith("miss") or name.startswith("ms"):
#     print("Hello madam, how are you? ")
# else:
#     name = name.capitalize()
#     print(f"Hi {name}! How are you?")

# Fun program
str = "a quick brown fox jumps over the lazy dog"
for c in "abcdefghijklmnopqrstuvwxyz":
    print(c, str.count(c))
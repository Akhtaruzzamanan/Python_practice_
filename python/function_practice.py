# def add(n1, n2):
#     return n1 + n2
# 
# number1 = int(input("Please insert a number: "))
# number2 = int(input("add another number: "))
# 
# sum = add(number1, number2)
# print("your number sumestion is: ", sum)

# import turtle

# turtle.speed(2)

# length = int(input("how big square you want to show? input here "))

# def draw_square(side_length):
#     for i in range(4):
#         turtle.forward(side_length)
#         turtle.left(90)
#     
# counter = 0
# while counter < 90:
#     draw_square(150)
#     turtle.color("orange")
#     turtle.right(4)
#     counter += 1
# def draw_tringle(side_length):
#     for i in range(3):
#         turtle.forward(side_length)
#         turtle.left(120)
# 
# 
# counter = 0
# while counter < 100:
#     draw_tringle(150)
#     turtle.right(5)
#     counter += 1
# 
# turtle.exitonclick()

# def myfunc(x = 100):
#     print("inside myfunc: ", x)
#     x =  10
#     print("inside of myfunc: ", x)
#     
# x = 20
# myfunc(x)
# print("Out side of x: ", x)
# def add_number(numbers):
#     result = 0
#     for number in numbers:
#         result = result + number
#     return result
# 
# number_list = [1, 3, 4, 2]
# summetion = add_number(number_list)
# print(summetion)
# 
# second_result = sum(number_list)
# print(second_result)

# অনুশীলনী ৬৫নং পৃষ্ঠার। 
def average_list(numbers):
    #Menual way for learning and understanding function
    result = 0
    length = len(numbers)
    for number in numbers:
        result += number
    average = result / length
    return average

    #alternet and easy way --->
#     result = sum(numbers)
#     length = len(numbers)
#     average = result / length
#     return average


number_list = [2, 3, 4, 5, 6]
number_average = average_list(number_list)
print(number_average)
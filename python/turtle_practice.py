import turtle

turtle.shape("turtle")

# Turtle make a square shape
'''turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)

turtle.exitonclick()'''

#Turtle make a triangle shape

'''turtle.forward(150)
turtle.left(120)
turtle.forward(150)
turtle.left(120)
turtle.forward(150)
turtle.left(120)

turtle.exitonclick()'''

#Turtle make a square shape with loop
'''for i in range(4):
    turtle.forward(100)
    turtle.left(90)'''

#Turtle make a dashed line
# turtle.speed(1)

# for n in range(20):
#     turtle.forward(10)
#     turtle.penup()
#     turtle.forward(3)
#     turtle.pendown()

#Turtle make a whill shape

# turtle.color("green")
# counter = 0
# while counter <= 36:
#     for i in range(4):
#         turtle.forward(100)
#         turtle.left(90)
#     turtle.right(10)
#     counter += 1
#     
# turtle.exitonclick()

height = 5
width = 5

turtle.penup()

for y in range(height):
    for x in range(width):
        turtle.dot()
        turtle.forward(20)
    turtle.backward(20 * width)
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)
    
turtle.exitonclick()

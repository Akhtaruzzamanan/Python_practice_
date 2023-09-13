import turtle
turtle.color("red", "yellow")
turtle.begin_fill()
while True:
    turtle.forward(200)
    turtle.left(170)
    if abs(turtle.position()) < 1:
        break
    
turtle.end_fill()
turtle.done()

# import turtle
# turtle.begin_fill()
# turtle.forward(200)
# turtle.left(120)
# turtle.forward(200)
# turtle.left(120)
# turtle.forward(200)
# turtle.end_fill()
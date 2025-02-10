"""
This example shows different speed controls of turtle. The function
turtle.speed() is used to change the speed of the turtle first from 10 (fast),
then to 1 (very slow) and finally to 0 (fastest). A square is drawn for each
of the speed.
"""

import turtle

# Draw a square using the turtle
def draw():
    print ("Speed is ", turtle.speed())
    for _ in range(4):
        turtle.left(90)
        turtle.forward(200)

# Move a normal turtle
draw()

# Move a fast turtle
turtle.reset()
turtle.speed(10) # Set the speed to fast
draw()

# Move a very slow turtle
turtle.reset()
turtle.speed(1) # Set the speed to very slow
draw()

# Move a fastest turtle
turtle.reset()
turtle.speed(0) # Set the speed to fastest
draw()

turtle.done()

"""
This example puts stamps of the turtle shape randomly in the window.
"""

import turtle
import random

# Set up the turtle
turtle.speed(0)
turtle.up()
turtle.hideturtle()

# Change the turtle shape to a turtle
turtle.shape("turtle")
turtle.shapesize(3, 3, 2)
turtle.color("black", "green")

# Stamp a hundred of the turtle
for _ in range(100):
    turtle.goto(random.randint(-250, 250), random.randint(-250, 250))
    turtle.left(random.randint(0, 359))

    turtle.stamp()

# Remove the turtles in reverse order
for _ in range(100):
    turtle.clearstamps(-1)

turtle.done()

"""
This example puts a big triangle stamp in the window.
"""

import turtle

# Hide the turtle
turtle.hideturtle()

# Change the turtle shape to a triangle
turtle.shape("triangle")
turtle.shapesize(10, 10)
turtle.color("red")

# Stamp the turtle shape at the current location
turtle.stamp()

turtle.done()

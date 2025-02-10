"""
This example changes the size of the shape line according to the
user input.
"""

import turtle

turtle.hideturtle()

# Change the turtle shape to a turtle and use black outline and red fill colour
turtle.shape("turtle")
turtle.color("black", "red")

# Get the user input for the size of the outline
line = input("Enter the width of the outline: ")

# Change the size according to the input values
turtle.shapesize(5, 5, line)
turtle.showturtle()

turtle.done()

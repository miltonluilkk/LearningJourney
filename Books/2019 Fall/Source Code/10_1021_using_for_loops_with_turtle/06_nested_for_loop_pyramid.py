"""
This is an example of using nested for loops to draw a pyramid of dots.
"""

import turtle

turtle.color("brown")
turtle.speed(0)      # Draw faster
turtle.up()          # Don't draw lines (but dots are not affected)
turtle.hideturtle()  # Hide the turtle

turtle.goto(0, 100)

size = 20

for i in range(0, 15, 2):
    for j in range(i + 1):
        turtle.dot(size)
        turtle.forward(size)

    # Move to the starting point of the next row
    turtle.backward(size * (i + 2))
    turtle.right(90)
    turtle.forward(size)
    turtle.left(90)

turtle.done()

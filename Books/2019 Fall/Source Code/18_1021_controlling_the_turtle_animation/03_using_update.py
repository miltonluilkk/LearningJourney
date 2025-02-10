"""
This example demonstrates the use of the tracer function so that no animation
is shown at all. Instead of turning the tracer to update the screen,
turtle.update() is used to update the turtle screen content every 4 squares.
"""

import turtle
import time

# Draw a square using the turtle
def draw():
    for _ in range(4):
        turtle.left(90)
        turtle.forward(200)

turtle.width(3)
turtle.tracer(False)

# Draw a set of squares without animation

for i in range(36):
    draw()
    turtle.left(10)

    if (i + 1) % 4 == 0:
        # Update the turtle screen after drawing every four squares
        turtle.update()

        # Wait for 1 second after showing the squares
        time.sleep(1)

turtle.done()

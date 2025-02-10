"""
This example uses the update function to make
an animation of a colourful set of squares.
"""

import turtle
import time

# Draw a square using the turtle
def draw():
    for _ in range(4):
        turtle.left(90)
        turtle.forward(200)

# Draw a set of squares
def draw_squares():
    colors = ["red", "orange", "yellow", "green",
              "lime green", "blue", "purple"]
    
    for i in range(36):
        turtle.color(colors[i % len(colors)])
        draw()
        turtle.left(10)

turtle.width(3)
turtle.tracer(False)

# Draw a rotating set of squares
while True:
    # Clear the previous squares
    turtle.clear()
    
    # Draw the set of squares
    draw_squares()

    # Update the screen
    turtle.update()

    # Change the rotation for the next set of squares
    turtle.left(10)

    # Wait for 0.05 second after showing the squares
    time.sleep(0.05)

turtle.done()

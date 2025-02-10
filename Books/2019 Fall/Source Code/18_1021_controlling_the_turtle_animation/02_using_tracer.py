"""
This example demonstrates the use of the tracer function so that no animation
is shown at all. The tracer, i.e. animation, is first turned off. Then a set
of squares is drawn using a for loop without any animation. Finally the squares
are immediately shown on the screen by enabling the tracer.
"""

import turtle

# Draw a square using the turtle
def draw():
    for _ in range(4):
        turtle.left(90)
        turtle.forward(200)

turtle.width(3)

# Draw a set of squares immediately without animation

turtle.tracer(False) # Turn off the tracer
for _ in range(36):
    draw()
    turtle.left(10)
turtle.tracer(True) # Turn on the tracer

turtle.done()

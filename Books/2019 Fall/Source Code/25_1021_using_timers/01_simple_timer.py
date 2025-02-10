"""
This example demonstrates the use of a timer to run code at exact timing. The
timer is set to run the draw function after 2 seconds.
"""

import turtle

def draw():
    turtle.up()
    turtle.goto(0, -100)
    turtle.down()
    turtle.circle(100)

# Set up a timer to run the draw function 2 seconds after starting this
# program
turtle.ontimer(draw, 2000)

turtle.done()

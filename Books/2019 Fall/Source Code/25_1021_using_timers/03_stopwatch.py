"""
This example creates a stopwatch program using a one second interval created
by the tick function.
"""

import turtle

# Draw the ticks of the stopwatch
def drawticks():
    turtle.left(180)
    for _ in range(60):
        # Move to the next tick position
        turtle.up()
        turtle.circle(100, 6)
        turtle.down()

        # Draw a tick
        turtle.right(90)
        turtle.forward(5)
        turtle.backward(5)
        turtle.left(90)
    turtle.right(90)

# Move the turtle to the next tick position
def tick():
    turtle.up()
    turtle.left(90)
    turtle.circle(100, -6) # Move 6 degrees clockwise, i.e. 1 second
    turtle.right(90)
    turtle.down()

    # Update the screen after moving the turtle
    turtle.update()

    # Move one tick one second later by running the function again
    turtle.ontimer(tick, 1000)

turtle.width(3)
turtle.shapesize(2, 2)
turtle.tracer(False)

turtle.up()
turtle.goto(0, 100)
turtle.down()

# Draw the ticks on the stopwatch
drawticks()

# Update the screen to show the ticks
turtle.update()

# Starts the stopwatch by moving the tick one second later
turtle.ontimer(tick, 1000)

turtle.done()

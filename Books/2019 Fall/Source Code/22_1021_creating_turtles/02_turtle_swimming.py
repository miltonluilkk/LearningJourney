"""
This example moves the turtle and changes the shape size along the way.
"""

import turtle

turtle.bgcolor("blue")
turtle.color("green")
turtle.up()

# Change the turtle shape to a turtle
turtle.shape("turtle")

while True:
    # Get the current turtle position and heading
    x, y = turtle.position()
    heading = turtle.heading()

    # Move the turtle
    turtle.forward(5)

    # Turn the turtle if it is at the boundary
    if heading == 0   and x > 200  or \
       heading == 90  and y > 200  or \
       heading == 180 and x < -200 or \
       heading == 270 and y < -200:
        turtle.setheading(heading + 90)

    # Change the size of the turtle based on its current position
    turtle.shapesize((turtle.xcor() % 60) / 60 + 2, \
                     (turtle.ycor() % 60) / 60 + 2)

"""
In this example a star is drawn by using a while loop.
First, we move the turtle to a position in the upper left of the screen.
Then we use a while loop to move the turtle forward and turn right 144 degrees.
We repeat the loop five times, to make a star.
"""

import turtle

turtle.width(5)     # Set the width to 5 pixels
turtle.up()         # Take the pen up (so no lines will be drawn)
turtle.goto(-200, 50)   # Move the turtle to a position in the top left area
turtle.down()       # Put the pen down (so now lines will be drawn)
turtle.color("orange", "purple")     # Set the line colour and the fill colour

# Initialize the side variable used by the while loop
side = 0

turtle.begin_fill() # We want this square to be filled

# While side is smaller than 5, the while loop will be executed
while side < 5:
    turtle.forward(400) # Move the turtle forward
    turtle.right(144)   # Move the turtle right 144 degrees

    side = side + 1   # Increase the side every time the loop is executed

turtle.end_fill()   # This triggers the filling of the square

turtle.done()

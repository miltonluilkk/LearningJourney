"""
In this example a square is drawn by using a while loop.
First, we move the turtle to a position in the upper left of the screen.
Then we use a while loop to move the turtle forward and turn right 90 degrees.
The loop is repeated four times, to make a square.  
"""

import turtle

turtle.width(5)     # Set the width to 5 pixels
turtle.up()         # Take the pen up (so no lines will be drawn)
turtle.goto(-200, 200) # Move the turtle to a position in the top left area
turtle.down()       # Put the pen down (so now lines will be drawn)
turtle.color("blue", "green")   # Set the line colour and the fill colour

# Initialize the side variable used by the while loop
side = 0

turtle.begin_fill() # We want this square to be filled

# While side is smaller than 4, the while loop will be executed
while side < 4:
    turtle.forward(400) # Move the turtle forward
    turtle.right(90)    # Move the turtle right 90 degrees
    
    # Increase the side every time that the loop is executed
    side = side + 1

turtle.end_fill()   # This triggers the filling of the square

turtle.done()

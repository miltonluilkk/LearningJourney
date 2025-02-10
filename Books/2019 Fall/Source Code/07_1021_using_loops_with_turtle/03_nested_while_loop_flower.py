# This example draws a pretty flower 

# We use four stages to build the flower:
#
# Stage 0: get the turtle graphics started
# Stage 1: the curved stem is created using part of a circle (no loops).
# Stage 2: the petals are drawn using a nested loop.
# Stage 3: the central part of the flower is drawn using a loop.

# -----------------------------------------
# Stage 0: get the turtle graphics started

# Bring the turtle graphics commands into Python
import turtle

# Use a reasonable drawing speed
turtle.speed(0)


# ---------------------------------------------------------------------
# Stage 1: the curved stem is created using part of a circle (no loops)

# First we draw the curved stem of the flower.
# To draw a curve, we can draw part of a circle.
# Here we draw 30 degrees of a very large circle.
turtle.width(20)
turtle.color("green")

turtle.up()             # Don't draw while we move the turtle
turtle.goto(100, -400)  # Move the turtle near the bottom right
turtle.left(90)         # Point the turtle upwards
turtle.down()           # Start drawing from now onwards
turtle.circle(1000, 30) # Draw circle with radius 1000 pixels

# Now we change angle a little bit,
# simply because the resulting flower head looks
# nice if we draw it after doing this
# (it doesn't make much difference if we don't do this)
turtle.left(30)


# -------------------------------------------------
# Stage 2: the petals are drawn using a nested loop

# Draw the petals using a red fill colour,
# with no outline colour
turtle.color("", "red")

# The outer while loop uses the inner while loop
# eight times, to draw eight petals in total

petal = 0 # Start with the first petal

while petal < 8: # Repeat for 8 petals in total

    # Move to the appropriate starting place for this petal
    turtle.up()
    turtle.forward(50)
    turtle.down()

    # The following inner loop draws one petal using 5 pieces.
    # Each piece is a red circle. Each red circle starts at a
    # different position to the previous one, and is bigger
    # than the previous one.
    
    petal_piece = 0 # Start with the first piece of the petal
    
    while petal_piece < 5: # Repeat for 5 pieces in total

        # First, go to the appropriate place.
        turtle.up()
        turtle.forward(petal_piece * 20) 
        turtle.left(90)
        turtle.down()

        # Second, draw the piece of the petal.
        # Each successive piece gets larger.
        turtle.begin_fill()
        turtle.circle(15 + petal_piece * 5)
        turtle.end_fill()

        # Third, go back to the starting position.
        # This is the opposite of the first stage.
        turtle.up()
        turtle.right(90)
        turtle.backward(petal_piece * 20)
        turtle.down()

        # Now we move on to the next piece
        # (in the following execution of the loop)
        petal_piece = petal_piece + 1


    # At this point we have finished drawing all 5
    # pieces of a petal. Now we go back to the position
    # we started at before we drew this petal.
    turtle.up()
    turtle.backward(50)
    turtle.down()

    # Now we get ready for drawing the next petal.
    # First, we change the angle of the turtle so
    # it is pointing to the correct direction for the
    # next petal. Each petal is 45 degrees further
    # than the previous petal.
    turtle.left(45)

    # Move on to construct the next petal
    # (in the following execution of the loop)
    petal = petal + 1



# At this point we have finished making all the red petals.
# Now we draw the middle of the flower.

# -------------------------------------------------------------
# Stage 3: the central part of the flower is drawn using a loop


# Let's use yellow circles and a thin line thickness
turtle.color("yellow4", "yellow")
turtle.width(2) 

# This is the radius of the first circle, the biggest circle
radius = 60     

# In the following loop we generate several circles.
# Each successive circle is a lot smaller than the previous circle.

# At the end of each loop, the radius will be reduced
# by the amount stored in this variable
radius_reduction = 3

# We keep drawing circles until we reach a small radius
while radius > 10:

    # First, move the turtle to the correct position
    # (Remember that to draw a circle using turtle.circle 
    # the turtle has to be moved to the side first).
    turtle.up()
    turtle.forward(radius)
    turtle.left(90)
    turtle.down()
    
    # Second, draw the yellow circle.
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

    # Third, go back to the original starting point.
    # This is the opposite of the first stage.
    turtle.up()
    turtle.right(90)
    turtle.backward(radius)
    turtle.down()

    # Now we adjust the size of the radius, for the
    # next circle that gets drawn (in the following
    # execution of the loop).
    radius = radius - radius_reduction

    # For a more natural effect, the circle radius
    # is not reduced by the same amount each time.
    # Instead, successive circles are reduced by larger amounts.
    radius_reduction = radius_reduction * 2

# Finished! Now let's hide the turtle so the result looks better
turtle.hideturtle()

turtle.done()

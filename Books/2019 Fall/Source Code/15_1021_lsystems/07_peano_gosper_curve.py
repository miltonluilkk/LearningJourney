import turtle

turtle.speed(0)
turtle.width(2)

# Ask for the number of iterations for the L-system
iterations = int(input("How many iterations do you want? "))
string = "X"

# Repeatedly apply the rules X -> X+YF++YF-FX--FXFX-YF+
#                            Y -> -FX+YFYF++YF+FX--FX-Y
for _ in range(iterations):
    result = ""
    for letter in string:
        if letter == "X":
            result = result + "X+YF++YF-FX--FXFX-YF+"
        elif letter == "Y":
            result = result + "-FX+YFYF++YF+FX--FX-Y"
        else:
            result = result + letter
    string = result

# Draw the resulting string
for letter in string:
    if letter == "F":
        turtle.forward(10)
    elif letter == "+":
        turtle.left(60)
    elif letter == "-":
        turtle.right(60)

turtle.done()

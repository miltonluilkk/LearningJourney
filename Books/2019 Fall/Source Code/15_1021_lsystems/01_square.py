import turtle

turtle.speed(0)
turtle.width(2)

# Ask for the number of iterations for the L-system
iterations = int(input("How many iterations do you want? "))
string = "F+F+F+F"

# Repeatedly apply the rule F -> FF
for _ in range(iterations):
    result = ""
    for letter in string:
        if letter == "F":
            result = result + "FF"
        else:
            result = result + letter
    string = result

# Draw the resulting string
for letter in string:
    if letter == "F":
        turtle.forward(10)
    elif letter == "+":
        turtle.right(90)

turtle.done()

import turtle

turtle.speed(0)
turtle.width(2)

# Ask for the number of iterations for the L-system
iterations = int(input("How many iterations do you want? "))
string = "F++F++F"

# Repeatedly apply the rule F -> F-F++F-F
for _ in range(iterations):
    result = ""
    for letter in string:
        if letter == "F":
            result = result + "F-F++F-F"
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

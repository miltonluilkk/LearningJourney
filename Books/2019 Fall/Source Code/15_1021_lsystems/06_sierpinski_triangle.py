import turtle

turtle.speed(0)
turtle.width(2)

# Ask for the number of iterations for the L-system
iterations = int(input("How many iterations do you want? "))
string = "A"

# Repeatedly apply the rules A -> B-A-B, B -> A+B+A
for _ in range(iterations):
    result = ""
    for letter in string:
        if letter == "A":
            result = result + "B-A-B"
        elif letter == "B":
            result = result + "A+B+A"
        else:
            result = result + letter
    string = result

# Draw the resulting string
for letter in string:
    if letter == "A":
        turtle.forward(10)
    elif letter == "B":
        turtle.forward(10)
    elif letter == "+":
        turtle.left(60)
    elif letter == "-":
        turtle.right(60)

turtle.done()

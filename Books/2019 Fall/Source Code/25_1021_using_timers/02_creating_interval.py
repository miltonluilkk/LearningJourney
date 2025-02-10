"""
This example demonstrates using turtle.ontimer() to build a text-based
stop watch program.
Note that the turtle window is not used in this example.
"""

import turtle

"""
A stop watch function to run for each time interval
"""
def stopwatch():
    global seconds
    print(seconds)
    seconds = seconds + 1

    turtle.ontimer(stopwatch, 1000)

seconds = 0
stopwatch()

turtle.done()

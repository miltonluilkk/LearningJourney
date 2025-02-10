"""
This example demonstrates using time.sleep() to build a stop watch.
"""

import time

seconds = 0
while True:
    print(seconds)
    seconds = seconds + 1

    time.sleep(1)

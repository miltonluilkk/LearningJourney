"""
This is an example of a while loop which finishes  
when the value of a variable is changed
"""

print("This is a great course!")

response = ''

while response != 'y':
    response = input('Do you agree? (y/n) ')

"""
This is an example of a while loop which finishes  
when the value of a variable is changed to a few
designated values
"""

print("This is a great course!")

response = ''

while response != 'y' and response != 'Y' and \
      response != 'yes' and response != 'Yes':
    response = input('Do you agree? (y/n) ')

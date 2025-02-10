# Demonstration of using lists and tuples in Python

# Create a list with three items
girlfriends = ["Stephy", "Sa", "Angela"]

# Print the current content of the list
print("Current content of the list is", girlfriends)
print()

# Ask for an index of the list
index = input("Please enter the index you want to change (0 - 2): ")
print()

index = int(index)

# Print the current value of the index
# The str() function changes the data type from a list to a string
print("Current value of index " + str(index) + " is " + girlfriends[index])
print()

# Ask for the new value of the index content
value = input("Please input a new value: ")
girlfriends[index] = value
print()

# Print the current content of the list
print("New value of the list is", girlfriends)
print()

# Create a tuple with five items
myfriend = ("John", 18, "CSE", 180, 70)

# Print the current content of the list
print("Current value of the tuple is", myfriend)
print()

# Ask whether you want to change the tuple
answer = input("Do you want me to try to modify the tuple (y or n)? ")
print()

if answer == "y":
    # Change the value of the tuple
    myfriend[2] = "ECE" # Not allowed, will give error

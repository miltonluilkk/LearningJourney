# This program shows some simple examples 
# of using the stack operations push 
# (called 'append' in Python) and pop.

# Create a list with two numbers in it
all_numbers = [11, 22]; 

print("The numbers in the list are", all_numbers)

# Now let's push three numbers on to the list
all_numbers.append(33)
all_numbers.append(44)
all_numbers.append(55)

print("Now, the numbers in the list are", all_numbers)

# Now let's pop four numbers off the list
all_numbers.pop()
all_numbers.pop()
all_numbers.pop()
all_numbers.pop()

print("Now, the numbers in the list are", all_numbers)
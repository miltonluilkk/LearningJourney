"""
This example reads data from a text file.

The text file contains 2 values on each row.
The first item is a letter/symbol, followed by a tab character.
The second item is some text, followed by the end of line character.

The two values are taken from the file and stored as a list.
The list is added at the end of a list of lists called 'rules'.
Each row of the file is stored as a separate list within 'rules'.

Example of the file line structure:

X	X+YF+
Y	-FX-Y
. . .

(a tab character separates each item in a row)

"""

# Initialize the rules
rules = []

filename = input("What rule file shall I read? ")
myfile = open(filename, "r") # Open the file for reading

# Now we go through each line in the file, one by one
for line in myfile: 

    # Read each line as a single rule
    line = line.rstrip()    # remove any spaces at the end

    # Line is currently a simple string
    print("line is", line)

    line = line.split("\t") # separate the two items

    # Line is now a list containing two items
    print("line is", line)
            
    # Add the rule (a list) at the end of the data structure
    rules.append(line)

    print()

# Close the file
myfile.close()

print("The data structure is ")
print(rules)

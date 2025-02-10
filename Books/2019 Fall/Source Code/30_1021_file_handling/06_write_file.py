"""
This example writes data to a text file.

The text file contains 2 values on each row.
The first item is a letter/symbol, followed by a tab character.
The second item is some text, followed by the end of line character.

The two items are taken from the data structure called 'rules'
and saved into the file, one line at a time.

Example of the file line structure:

X	X+YF+
Y	-FX-Y
. . .

(a tab character separates each item in a row)

"""

# Initialize the rule list of lists
rules = [["X", "X+YF+"],
         ["Y", "-FX-Y"]]

filename = input("What rule file shall I create? ")
myfile = open(filename, "wt") # Open the file for reading

# Now we go through each item in the data structure, one by one
for rule in rules: 

    # Make a string for one line, in the correct format
    one_line = rule[0] + "\t" + rule[1] + "\n"

    # Save the string to the file
    myfile.write(one_line)

# Close the file
myfile.close()

#-----------------------------------------------------------------------------
# Name:        String Manipulation (stringManipulation.py)
# Purpose:     Different ways to manipulate Strings (and some file reading)
#
# Author:      Mr. Kowalczewski
# Created:     31-Jan-2021
# Updated:     21-Jun-2021
#-----------------------------------------------------------------------------

# Opens the file test.txt in "r"ead mode.  Always be sure to close your file!
# Look up "Python file reading/writing" to see more.
file = open("test.txt", 'r')
fileContents = file.readlines()
file.close()

# What type of variable is fileContents?
print(type(fileContents))

# What does it look like?
print(fileContents)

# Each item in the list is a string.  And remember that you can access individual characters in a string (like a list) - but not modify them.

# The newline character (\n) counts as ONE CHARACTER - even though it looks like 2.

# How would we know to print up to item 12 if we didn't already know the length??
print(fileContents[0][0:12])
print(len(fileContents[0]))

# Visit https://www.w3schools.com/python/python_ref_string.asp for a long list of different ways you can modify/analyze strings.

# Anything that returns True/False can be used in if statements

famousQuote = "i'll try spinning - that's a good trick!"
numericString = '12a345'

famousQuote = famousQuote.capitalize()
print(famousQuote)

print(famousQuote.count('spin'))

if famousQuote.endswith("!"):
	print("This quote is exciting!")

print(famousQuote.isalnum())
print(numericString.isnumeric())





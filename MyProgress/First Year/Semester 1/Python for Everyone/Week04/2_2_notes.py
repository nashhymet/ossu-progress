print("Output:")
print("----------------------------------")
print("\n")
### Expressions Part 2
## Numeric Expressions
# ----------------------------------------------
# Outputs: 4
#xx = 2
#xx = xx + 2
#print(xx)

# Outputs: 5280
#yy = 440 * 12
#print(yy)

# Outputs: 5.28
#yy = 440 * 12
#zz = yy / 1000
#print(zz)

# Outputs: 3
#jj = 23
#kk = jj % 5
#print(kk)

# Outputs: 64
#print(4 ** 3) # ** is the power operator
# ----------------------------------------------

## Order of Evaluation
# When we string operators together -
# Python must know which one to do first

# This is call "operator precedence"

# Which operator "takes precedence" over the others?

# Below would output: 6.999744
#x = 1 + 2 * 3 - 4 / 5 ** 6

# How it's working is this:
# Parentheis
# Power
# Multiplication
# Addition
# Left to Right

# This is for debug:
# print(x)
# ----------------------------------------------

## Type Matters
# Python knows what "type" everything is

# Some operations are prohibited

# You cannot "add 1" to a string

# We can ask Python what type something is by using the
# type() function

# Example 1 - Outputs: hellothere
#eee = 'hello' + 'there'
#print(eee)

# Example 2 - Will produce a Traceback error
#eee = 'hello' + 'there'
#eee = eee + 1
#print(eee)
# ----------------------------------------------

## Several Types of Numbers
# Numbers have two main types
# - Integers are whole numbers:
#   -14, -2, 0, 1, 100, 401233

# - Floating Point Numbers have decimal parts:
#   -2.5, 0.0, 98.6, 14.0

# There are other number types - they are variations
# on float and integer
# ----------------------------------------------

## Type Conversions
# When you put an integer and floating point in an Expression
# the integer is implicitly converted to a float

# You can control this with the built-in functions int() and float()
# Example 3 - Outputs: 199.0
#print(float(99) + 100)
#i = 42 # this gets outputted as 42.0
#type(i)
#f = float(i) # using this line
#print(f)
#type(f)
# ----------------------------------------------

## String Conversions
# You can also use int() and float() to convert
# between strings and integers

# You will get an error if the string does not contain
# numeric characters

# Example 5 - Outputs a Traceback error
#sval = '123'
#type (sval)
#print(sval + 1)

# Example 6 - Outputs: 124
#sval = '123'
#type (sval)
#ival = int(sval)
#type(ival)
#print(ival + 1)

# Example 7 - Outputs a Traceback error
#nsv = 'hello bob'
#niv = int(nsv) # requires an int
# ----------------------------------------------

## User Input
# We can instruct Python to pause and read data from
# the user using the input() function

# The input() function returns a string

# Example 8 - Asks you who you are and prints a welcome message
#nam = input('Who are you?')
#print('Welcome', nam)
# ----------------------------------------------



print("----------------------------------\n")
print("The end of the line: nothing is here")

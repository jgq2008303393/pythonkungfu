#!/usr/bin/env python

# %s - String (or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers
# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
# %x/%X - Integers in hex representation (lowercase/uppercase)

# Our variable
data = ("John", "Doe", 53.44)
format_string = "Hello"

# Print them with formatting
print "%s %s %s. Your current balance is %.2f$." % (format_string, data[0], data[1], data[2])
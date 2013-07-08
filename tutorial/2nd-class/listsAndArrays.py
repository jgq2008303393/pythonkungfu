#!/usr/bin/env python

# Array declaration
numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# Second name is the second value of `names' array
second_name = names[1]

# Fill `numbers' array with 1, 2, and 3
numbers.append(1)
numbers.append(2)
numbers.append(3)

# Fill `strings' array with "Hello", and "world"
strings.append("Hello")
strings.append("world")

print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)
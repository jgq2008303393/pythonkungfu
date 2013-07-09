#!/usr/bin/env python

numbers = [
    951, 402, 984, 651, 360,
    692, 408, 319, 601, 485,
    980, 507, 725, 547, 544
]

# Loop through and print out all even numbers from the numbers list in the same order they are received.
# Don't print any numbers that come after 507 in the sequence.
for i in numbers:
    print i
    if i == 507:
        break
#!/usr/bin/env python

number = 16
second_number = []
first_array = [1, 2, 3]
second_array = [1, 2]

if number > 15:
    print "number is greater than 15"
if first_array:
    print "first_array should not null, empty, or false"
if len(second_array) == 2:
    print "second_array contains two elements"
if len(first_array) + len(second_array) == 5:
    print "The length of first_array plus length of second_array equals to 5"
if first_array and first_array[0] == 1:
    print "first_array should not null, empty, or false and the first element of first_array is 1"
if not second_number:
    print "Second number should be null, empty, or false"
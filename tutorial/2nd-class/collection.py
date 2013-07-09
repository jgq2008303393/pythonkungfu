#!/usr/bin/env python
asbak = ["Abu", "Puntung", "Sampah"]

print asbak
for i in xrange(0, len(asbak)):
    print asbak[i]

beberapaAngka = [11, 3, 7, 9]

# Tambahin 10 ke dalam array beberapaAngka
beberapaAngka.append(10)


def arrayOperation(array, operation):
    a = int(0)
    for x in xrange(0, len(array)):
        # Handling error
        if type(array[x]) != int:
            return "The element is not a number"
        else:
            a += array[x]
    if (operation == "sum"):
        return a
    if(operation == "avg"):
        return a / len(array)
    if(operation == "mul"):
        a = int(array[0])
        for x in xrange(1, len(array)):
            # Handling error
            if type(array[x]) != int:
                return "The element is not a number"
            else:
                a = a * array[x]
        return a
    else:
        return "Invalid operation!"

print beberapaAngka
print "Sum = %d" % arrayOperation(beberapaAngka, "sum")
print "Average = %.2f" % arrayOperation(beberapaAngka, "avg")
print "Multiply = %d" % arrayOperation(beberapaAngka, "mul")

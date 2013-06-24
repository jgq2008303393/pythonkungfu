#!/usr/bin/env python


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
        return float(a) / len(array)
        print arrayOperation(myArray, "avg")
    if(operation == "mul"):
        a = int(array[0])
        for x in xrange(1, len(array)):
            # Handling error
            if type(array[x]) != int:
                return "The element is not a number"
            else:
                a = a * array[x]
        return a
        print arrayOperation(myArray, "mul")
    else:
        return "Invalid operation!"

print "Berapa angka yang mau dioperasikan?"
x = int(raw_input())
number=[]
for x in xrange(0, x):
    number.append(int(raw_input("Angkanya : ")))
  
operasi = str(raw_input("Operasi yang akan dijalankan :"))
if (operasi == "sum"):
    print arrayOperation(number, "sum")
if (operasi == "avg"):
    print arrayOperation(number, "avg")
if (operasi == "mul"):
    print arrayOperation(number, "mul")

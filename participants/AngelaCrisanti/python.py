#!/usr/bin/env python
import sys


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
    if(operation == "mul"):
        a = int(array[0])
        for x in xrange(1, len(array)):
            # Handling error
            if type(array[x]) != int:
                return "The element is not a number"
            else:
                a = a * array[x]
        return a
        # print arrayOperation(array, "mul")
    else:
        return "Invalid operation!"

# print "Berapa angka yang mau dioperasikan?"
# x = int(raw_input())
number = []
# for x in xrange(0, x):
#     number.append(int(raw_input("Angkanya : ")))
i = int(raw_input("Berapa angka yang mau dioperasikan? "))
for x in xrange(0, i):
    number.append(int(raw_input("[%d] Angkanya: " % x)))


# operasi = str(raw_input("Operasi yang akan dijalankan: "))
# print arrayOperation(number, str(raw_input("Operasi yang akan dijalankan: ")))
# if (operasi == "sum"):
#     print arrayOperation(number, "sum")
# if (operasi == "avg"):
#     print arrayOperation(number, "avg")
# if (operasi == "mul"):
#     print arrayOperation(number, "mul")

print "1. Penjumlahan\n2. Rata-rata\n3. Perkalian"
operasi = int(raw_input("Operasi yang akan dijalankan: "))

if (operasi == 1):
    print arrayOperation(number, "sum")
    sys.exit(0)
if (operasi == 2):
    print arrayOperation(number, "avg")
    sys.exit(0)
if (operasi == 3):
    print arrayOperation(number, "mul")
    sys.exit(0)
else:
    print arrayOperation(number, "invalid")
    sys.exit(1)

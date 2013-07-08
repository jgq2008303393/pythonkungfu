#!/usr/bin/env python
import sys;

names = ["blusp10it", "red-dragon"];
nilai = [];
temp = 0;
minPass = 6.5;
average = 0;

def getIndex(array, name):
    for i in xrange(0, len(array)):
        if array[i] == name:
            return i;
    return False;

def amIPass(average):
    if average >= minPass:
        return "Yes"
    else:
        return "No"

name = raw_input("Masukkan nama: ");
index = getIndex(names, name);

if type(index) == int:
    nameFromArray = names[index];
else:
    print "Not found";
    sys.exit(1);

print nameFromArray;
# for (int x = 0; x < 5; x++) {  }
for x in xrange(0, 5):
    temp = int( raw_input("[%d] Input grade for %s: " % (x, nameFromArray)) );
    # temp = int(temp);
    nilai.append(temp);
    # Or it can be like this
    # nilai.append(int( raw_input("[%d] Input grade for %s: " % (x, nameFromArray)) ));

total = sum(nilai);
average = total / len(nilai);

print "Total for %s: %d" % (nameFromArray, total);
print "Nilai rata-rata %s: %d" % (nameFromArray, average);
print "Is %s pass? %s" % (nameFromArray, amIPass(average));

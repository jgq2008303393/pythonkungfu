#!/usr/bin/env python

asbak = ["abu","puntung","ludah","anu","ijuk",3,4];
print asbak;

for i in xrange(0, len(asbak)):
	print asbak[i];

def cetak(arg):
	print arg;

beberapa = [12,3,7,9];
def tambah(agr1,arg2,arg3,arg4):
	print arg1+arg2+arg3+arg4;

tambah(12,3,7,9);

# tambahin angka 10 ke dalam array beberapaAngka
beberapaAngka.append(10);

def sumarray(array):
	a = int(0);
	if type(array[0]) != int:
		return "1. the element is not an integer";
	else:
		a = array[0];
	for x in xrange(1, len(array)):
		if type(array[x]) != int:
			return "2. the element is not an integer";
	else:
		a = a + array[x];
	return a;

	print sumarray(beberapaAngka);
#!/usr/bin/env python
import sys


def check(pilihan):
    try:
        return int(pilihan)
    except:
        print "Input salah: %s" % pilihan
        sys.exit(1)


def calculator(operasi, bilangan1, bilangan2):
    if (operasi == 1):
        return [bilangan1, bilangan2, bilangan1 + bilangan2, "+"]
    if (operasi == 2):
        return [bilangan1, bilangan2, bilangan1 - bilangan2, "-"]
    if (operasi == 3):
        return [bilangan1, bilangan2, bilangan1 * bilangan2, "*"]
    if (operasi == 4):
        return [bilangan1, bilangan2, float(bilangan1) / float(bilangan2), "/"]
    else:
        print "Operasi salah: %s" % operasi
        sys.exit(1)

print "1. Tambah\n2. Kurang\n3. Kali\n4. Bagi"
hasil = calculator(check(raw_input("Masukan operasi: ")), check(raw_input("Masukan bilangan pertama: ")), check(raw_input("Masukan bilangan kedua: ")))
print "Hasil: {0} {3} {1} = {2:.2f}".format(hasil[0], hasil[1], hasil[2], hasil[3])

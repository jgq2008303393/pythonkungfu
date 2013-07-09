#!/usr/bin/env python


def cetak(anu):
    print anu


def tambah(arg1, arg2, arg3):
    print arg1 + arg2 + arg3


def kurang(arg1, arg2):
    print arg1 - arg2


def angkaKuadrat(arg):
    return arg**2


def angkaDiKaliDua(arg):
    return arg*2

tambah(3, 4, 3)
kurang(2, 5)
angkaGue = angkaKuadrat(angkaDiKaliDua(2))
cetak(angkaGue)
# smart = tambah(kurang(3, 2), 2, 2)
# cetak(smart)

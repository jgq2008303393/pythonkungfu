#!/usr/bin/env  python


class OS(object):
    def __init__(self, nama, berbasis, free):
        self.nama = nama
        self.berbasis = berbasis
        self.free = free

    def setNama(self, question, nama, lnx):
            self.question = question
            self.nama = nama
            self.lnx = lnx

    def bersuara(self, suara1, suara2):
                self.suara1 = suara1
                self.suara2 = suara2
                # print "%s: %s" % (self.nama, self.suara)

linux = OS ("LINUX", "open source", "free")
print linux.nama, linux.berbasis, linux.free
linux.setNama("Question:", "What do you like", "LINUX...?")
print linux.question, linux.nama, linux.lnx
# print linux.suju
linux.bersuara ("Answer:", "of course...!")
print linux.suara1, linux.suara2

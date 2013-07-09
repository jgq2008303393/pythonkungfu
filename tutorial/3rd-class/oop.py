#!/usr/bin/env python


class Binatang(object):
    def __init__(self, nama, makanan, isJinak):
        # print "%s dibuat!!!" % (nama)
        self.isJinak = isJinak
        self.nama = nama
        self.makanan = makanan

    def setNama(self, nama):
        self.nama = nama

    def bersuara(self, suara):
        self.suara = suara
        print "%s: %s" % (self.nama, self.suara)

# Instantiating Class / Object
kucing = Binatang("Kucing", "Ikan", "Jinak")
# print "%s makan %s. Dia itu %s." % (kucing.nama, kucing.makanan, kucing.isJinak)
print kucing.nama
# Override attribute
# kucing.nama = "Anjing"
kucing.setNama("Anjing")
# kucing = Binatang("Anjing", "Ikan", "Jinak")
print kucing.nama
# kucing.bersuara("Guk guk")

#!/usr/bin/env python 

# class

class Dota(object):
	def __init__(self,nama, skill, tipe):
		self.tipe = tipe
		self.nama = nama
		self.skill = skill

	def SetNama(self, nama):
		self.nama = nama
		
	def Bersuara(self, suara):
		self.suara = suara
		print "%s: %s" % (self.nama, self.suara)
# instantiating class / opjec 
Hero = Dota("Lion", "stun", "tangker")
print Hero.nama
print Hero.skill, Hero.tipe

Hero.SetNama("Rikimaru")
print Hero.nama

Hero.Bersuara('slawww')
print Hero.suara
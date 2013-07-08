#!/usr/bin/env python

class Dota(object):
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setVision(self, vision):,
        self.vision = vision

    def getVision(self):
        return self.vision

class Hero(Dota):
    def __init__(self, name):
        self.name = name

    def dump(self):
        print "Name: %s\nVision: %s" % (self.name, self.vision)

Viper = Hero ("Viper")
Viper.setVision ("Kills...again...again and again...!")
Viper.dump()

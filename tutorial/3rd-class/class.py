#!/usr/bin/env python


class Human():
    def __init__(self, name, alias):
        self.name = name
        self.alias = alias

    def getName(self):
        return self.name

    def getAlias(self):
        return self.alias

    def setName(self, this, value):
        this.name = value

    def setAlias(self, this, value):
        this.alias = value


class Child(Human):
    def __init__(self):
        print "Creating new Child"

    def prototypeGetName(self):
        return self.getName()


zeek = Human("Krisan Alfa Timur", "Zeek")
# zeek.setName(zeek, "Alfa")
print zeek.getName()
print zeek.getAlias()

child = Child()
child.setName(child, "Anu")
child.setAlias(child, "Ini")
print child.getName()
print child.getAlias()
# print child.prototypeGetName()

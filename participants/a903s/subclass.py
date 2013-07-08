#!/usr/bin/env  python

#class utama
class OS(object):
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setVersion(self, version):
        self.version = version

    def getVersion(self):
        return self.version

    def setFamily(self, family):
        self.family = family

    def getFamily(self):
        return self.family


#sub class
class Linux(OS):
    def __init__(self, name):
        self.name = name
        # self.version = version
        # self.family = family

    def dump(self):
        print "Name: %s\nVersion: %s\nFamily: %s" % (self.name, self.version, self.family)

#Interface
ubuntu = Linux ("Ubuntu")
ubuntu.setVersion("13.04")
ubuntu.setFamily("Debian")
ubuntu.dump()

# alternatif
# ubuntu = Linux ("ubuntu", "13.05", "Debian")
# print ubuntu.name
# print ubuntu.version
# print ubuntu.family

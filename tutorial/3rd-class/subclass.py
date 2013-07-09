#!/usr/bin/env python


# Parent Class
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


# Child ClassOS
class Linux(OS):
    def __init__(self, name):
        self.name = name

    def dump(self):
        print "Name: %s" % self.name
        print "Version: %s" % self.version
        print "Family: %s" % self.family

# Inheritance
ubuntu = Linux("Ubuntu")
ubuntu.setVersion("13.04")
ubuntu.setFamily("Debian")
ubuntu.dump()

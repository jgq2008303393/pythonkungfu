# #!/usr/bin/env python

 class OS(object):
 	def __init__(self,nama):
 		self.nama = nama

 	def getName(self):
 		return self.name

 	def setVersion(self, version):
 		self.version = version

 	def getVersion(self):
 		return self.version

 	def setFamily(self, family):
 		self.family = family

 	def family(self):
		return self.family

class Linux(OS):
	def __init__(self, name, version, family):
		self.name = name
		self.version = version
		self.family = family

# 	def dump(self):
# 		print "nama: %s" % self.nama
# 		print "Version: %s" % self.version
# 		print "Family: %s" % self.family

# ubuntu = Linux("ubuntu")
# ubuntu.setVersion("13.04")
# ubuntu.setFamily("Debian")
# ubuntu.dump()

ubuntu = Linux("ubuntu","13.04","Debian")
print "Nama:", ubuntu.name
print "Versi:", ubuntu.version
print "family:", ubuntu.family

# -*- coding: utf-8 -*-
# Licensed under GNU General Public License v3
class dslTag(object):
	def getType(self):
		if self.line.startswith("@!"):
			return "CommandTag"
		elif self.line.startswith("@#"):
			return "GroupTag"
		elif self.line.startswith("@?"):
			return "VarTag"
		elif self.line.startswith("@"):
			return "TranslateTag"
		else:
			raise ValueError("The string must start with the character 0x40 or '@'")
	def getTitle(self):
		phrase = ""
		for x in self.line:
			if x == "@" or x == "!" or x == "?" or x == "#":
				continue
			elif x == " ":
				return phrase
			else: 
				phrase = phrase + x
	def getValue(self):
		phrase = ""
		flag = False # If true, it means that the variable x contains a character of the value of a disline tag
		for x in self.line:
			if x == "@" or x == "!" or x == "?" or x == "#":
				if flag == False:
					continue
				else:
					phrase = phrase + x
			elif x == " ":
				if flag == False:
					flag = True
					continue
				else:
					phrase = phrase + x
			else:
				if flag == False:
					continue
				else:
					phrase = phrase + x
		return phrase
	def __init__(self, line):
		if type(line) == str:
			self.line = line
			self.type = self.getType()
			self.title = self.getTitle()
			self.value = self.getValue()
		else:
			raise TypeError("The argument must be of type 'string'")
def infoprog():
	versionarray = {
		"version": "2.0",
		"lang": "Python",
		"author": "Giovanni Alfredo Garciliano Diaz",
		"basedon": "Based on a work of Daniel Clemente Laboreo (http://danielclemente.com/dislines/index.es.html)",
		"license": "GNU General Public License v3",
		"url": "http://giobeatle1794.esy.es/dislines",
		"createdusing": "gedit, python"
	}
	return versionarray
ggg = dslTag("@!es Hola mundo!")
print("Line: "+ggg.line)
print("Type: "+ggg.type)
print("Title: "+ggg.title)
print("Value: "+ggg.value)
#def dislines(filename,lang):
#	counter = 0
#	filedsl = open(filename, "r")
#	for getline in archivo.readlines():
#		line[counter] = getline
#		counter++
#	filedsl.close()
	# The parsing process begins here

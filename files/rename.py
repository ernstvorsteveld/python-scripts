#!/usr/bin/env python

import os
import sys

class FileDetails:
	def __init__(self, file_name, serialNumber):
		self.file_name = file_name
		self.serialNumber = serialNumber		

	def getNewFileName(self, printIt):
		self.findFileDetails()
		if(printIt):
			print 'rename: ' + self.file_name + ' into: ' + self.name + self.serialNumber + '-' + self.number + self.fileParts[1]
		else:
			print 'implement rename for: ' + self.file_name

	def findFileDetails(self):
		self.number=''
		self.fileParts = os.path.splitext(self.file_name)
		fileName = self.fileParts[0]
		while(True):
			lastCharacter = self.getLastCharacter(fileName)
			if(lastCharacter.isdigit()):
				self.number += lastCharacter
				fileName = self.removeLastCharacter(fileName)
				self.name = fileName
			else:
				return

	def getLastCharacter(self, characters):
		return characters[(len(characters) - 1):]

	def removeLastCharacter(self, characters):
		return characters[:(len(characters) - 1)]


def rename(directory, serialNumber, printIt):
	print directory
	for file_name in os.listdir(directory):
		print 'working on file: ' + file_name
		fileDetails = FileDetails(file_name, serialNumber)
		fileDetails.getNewFileName(printIt)


directory = sys.argv[1]
serialNumber = sys.argv[2]
execute = sys.argv[3] == '1'

rename(directory, serialNumber, execute)



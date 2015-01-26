#!/usr/bin/env python

import os
import sys

class FileDetails:
	def __init__(self, directory, file_name, serialNumber):
		self.directory = directory
		self.file_name = file_name
		self.serialNumber = serialNumber		

	def rename(self, execute):
		self.findFileDetails()
		if(execute):
			print 'file_name: ' + self.getOldName()
			print 'new: ' + self.getNewName()
			os.rename(self.getOldName(), self.getNewName())
		else:
			print 'rename: ' + self.getOldName() + ' to: ' + self.getNewName()

	def findFileDetails(self):
		self.number=''
		self.fileParts = os.path.splitext(self.file_name)
		fileName = self.fileParts[0]
		ready = False
		while(not ready):
			lastCharacter = self.getLastCharacter(fileName)
			if(lastCharacter.isdigit()):
				self.number += lastCharacter
				fileName = self.removeLastCharacter(fileName)
				self.name = fileName
			else:
				ready = True

	def getLastCharacter(self, characters):
		return characters[(len(characters) - 1):]

	def removeLastCharacter(self, characters):
		return characters[:(len(characters) - 1)]

	def getNewName(self):
		return self.directory + ('/', '')[directory.endswith('/')] + self.name + self.serialNumber + '-' + self.number + self.fileParts[1]

	def getOldName(self):
		return self.directory + ('/', '')[directory.endswith('/')] + self.file_name		


class Skip:
	def __init__(self, skipFilenames):
		self.skip = skipFilenames

	def isSkip(self, file_name):
		return file_name in self.skip


def rename(directory, serialNumber, printIt, skip):
	print 'rename, working on directory: ' + directory
	for file_name in os.listdir(directory):
		if(skip.isSkip(file_name)):
			continue;
		if(os.path.isdir(file_name)):
			print 'working on directory: ' + file_name
			newDirectory = directory + ('/', '')[directory.endswith('/')] + file_name
			os.chdir(directory)
			rename(newDirectory, serialNumber, printIt, skip)
			os.chdir('..')
		else:
			print 'working on file: ' + file_name
			print 'in directory: ' + directory
			fileDetails = FileDetails(directory, file_name, serialNumber)
			fileDetails.rename(printIt)


directory = sys.argv[1]
serialNumber = sys.argv[2]
execute = sys.argv[3] == '1'
skip = Skip('.DS_Store')

rename(directory, serialNumber, execute, skip)



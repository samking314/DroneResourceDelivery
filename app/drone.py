#
#	drone.py defines the class for a Drone object
#
#	created by: Samuel King
#

import getRandomData

class Drone :
	def __init__ ( self ) :
		self.name = "drone"
		self.x = 0
		self.y = 0
		self.z = 100

	def printSelf ( self ) :
		print( "Hello my name is " + self.name + " and I am at coordinates (" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")" )

	def getHeight ( self ) :
		return self.y

	def getLocation ( self ) :
		return [ self.x, self.y, self.z ]

	def changeLocation ( self, newLocation ) :
		self.x = newLocation.x
		self.y = newLocation.y
		self.z = newLocation.z

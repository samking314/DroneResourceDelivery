#
#	drone.py defines the class for a Drone object
#
#	created by: Samuel King
#

import getRandomData

class Drone :
	
	name = "drone"

	def __init__ ( self ) :
		self.__x = 0
		self.__y = 0
		self.__z = 100

	def __str__ ( self ) :
		return "Hello my name is " + __class__.name + " and I am at coordinates (" + str(self.__x) + ", " + str(self.__y) + ", " + str(self.__z) + ")"

	def getHeight ( self ) :
		return self.__y

	def getCurrentLocation ( self ) :
		return [ self.__x, self.__y, self.__z ]

	def changeCurrentLocation ( self, newLocation ) :
		self.__x = newLocation.x
		self.__y = newLocation.y
		self.__z = newLocation.z

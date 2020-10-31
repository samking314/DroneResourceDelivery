#
#	field.py defines the class for a Field object
#
#	created by: Samuel King
#

from . import getRandomData, drone

class Field( object ) :

	name = "The Highway"

	def __init__ ( self ) :

		# create only one drone
		self.createSingleDrone()

		# create field floor
		self.__xLen = 10
		self.__yLen = 10
		self.__zLen = 10
		self.__fieldFloor = getRandomData.createFieldFloor( self.__xLen, self.__yLen, self.__zLen )

		# create locations where items need to be picked up at
		self.__itemLocations = [ getRandomData.createOneItemLocation( self ) ]

	def createDroneFleet ( self ) :
		self.drones = [ 0 for x in range( 10 ) ]
		for i in range( 10 ):
			self.drones[i] = drone.Drone()

	def createSingleDrone ( self ) :
		self.drones = [ drone.Drone() ]

	# getter methods
	def getxLen ( self ) :
		return self.__xLen

	def getyLen ( self ) :
		return self.__yLen

	def getzLen ( self ) :
		return self.__zLen

	def getFieldFloor ( self ) :
		return self.__fieldFloor

	def getItemLocations ( self ) :
		return self.__itemLocations

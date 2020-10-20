#
#	field.py defines the class for a Field object
#
#	created by: Samuel King
#

from drone import Drone
import getRandomData

class Field :
	def __init__ ( self ) :
		self.name = "The Highway"
		self.createDroneFleet()
		self.xLen = 100
		self.yLen = 100
		self.zLen = 100
		self.fieldFloor = getRandomData.createFieldFloor( self.xLen, self.yLen, self.zLen )
		self.itemLocations = getRandomData.createItemLocations( 10, self )

	def createDroneFleet ( self ) :
		self.drones = [ 0 for x in range( 10 ) ]
		for i in range( 10 ):
			self.drones[i] = Drone()

# field = Field()

# print(str(field.itemLocations))
# print(str(field.fieldFloor))

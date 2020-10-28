#
#	item.py defines the class Item
#
#	created by: Samuel King
#

import getRandomData
import bson

class Item :
	
	def __init__ ( self ) :
		self.name = "item #" + str( bson.objectid.ObjectId() )

	def __str__ ( self ) :
		return "I am " + self.name

	def addRandomStartLocation ( self, field ) :
		self.__startLocation = getRandomData.createOneItemLocation( field )

	def getStartLocation ( self ) :
		return self.__startLocation

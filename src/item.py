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

	def addRandomStartLocation ( self, field ) :
		self.startLocation = getRandomData.createOneItemLocation( field )

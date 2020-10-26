#
#   testRando.py tests randomly calculated data
#
#   create by: Samuel King
#

import unittest
from random import randint
import sys
sys.path.append('../')
from src import getRandomData
from src.field import Field
from src.item import Item

class TestRandomData( unittest.TestCase ) :
	
	def createfieldfloor( self, XLen, YLen, ZLen ) :
		pointsMatrix = getRandomData.createFieldFloor( XLen, YLen, ZLen )
		filled = True
		for i in range( len( pointsMatrix ) ) :
			count = 0
			for j in range( len( pointsMatrix[i] ) ) :
				count += 1
			if count != YLen :
				filled = False
				break
		self.assertTrue( filled )

	def createitemlocations( self, numOfItems ) :
		field = Field()
		locations = field.itemLocations
		count = 0
		for i in range( len( locations ) ) :
			count += 1
		self.assertEqual( count, 10 )

	# test field floor for completeness
	def test_createfieldfloor( self ) :
		for x in range( 0, 10 ) :
			self.createfieldfloor( 100, 100, 100 )

	# test all items were created
	def test_createitemlocations( self ) :
		for x in range( 0, 10 ) :
			self.createitemlocations( 10 )

	# test create an item with random location
	def test_createoneitemlocation( self ) :
		field = Field()
		item = Item()
		item.addRandomStartLocation(field)
		self.assertTrue( item.startLocation != ( 0, 0, 0 ) )






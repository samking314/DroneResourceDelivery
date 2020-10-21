#
#   testRando.py tests randomly calculated data
#
#   create by: Samuel King
#

import unittest
from random import randint
import sys
sys.path.append('../')
import getRandomData
from field import Field

class MyTest( unittest.TestCase ) :
	def test( self ) :
		test1( self )
		test2( self )

# test field floor for completeness
def testCreateFieldFloor( self, XLen, YLen, ZLen ) :
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

# test all items were created
def testCreateItemLocations( self, numOfItems ) :
	field = Field()
	locations = field.itemLocations
	count = 0
	for i in range( len( locations ) ) :
		count += 1
	self.assertEqual( count, 10 )

def test1( self ) :
	for x in range( 0, 10 ) :
		testCreateFieldFloor( self, 100, 100, 100 )

def test2( self ) :
	for x in range( 0, 10 ) :
		testCreateItemLocations( self, 10 )

def main() :
	unittest.main()

if __name__ == '__main__' :
	main()

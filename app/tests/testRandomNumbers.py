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

class MyTest( unittest.TestCase ) :
	def test( self ) :
		test1( self )

def testGetRandoItems( self, numOfItems, XLen, YLen, ZLen ) :
	pointsArr = set()
	pointsArr = getRandomData.getRandomLocations( numOfItems, XLen, YLen, ZLen )
	self.assertEqual( len( pointsArr ), numOfItems )

def test1( self ) :
	for x in range( 0, 10 ) :
		testGetRandoItems( self, randint(5, 30), randint(5, 30), randint(5, 30), randint(5, 30) )

def main() :
	unittest.main()

if __name__ == '__main__' :
	main()

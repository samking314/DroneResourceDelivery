#
#   testRando.py tests randomly calculated data
#
#   create by: Samuel King
#

import unittest
from random import randint
import sys
sys.path.append('../')
from lib import getRandomData
from lib.findPath import Path

class TestFindPath( unittest.TestCase ) :

	def createOptimalPath( self ) :
		path = Path()
		path.findOverallPath()
		fieldFloor = path.getFieldFloor()
		pathCoords = path.getFinalPathCoords()
		for x in range( len( pathCoords ) ) :
			point = pathCoords[x]
			self.assertTrue( point[2] > fieldFloor[ point[0] ][ point[1] ] )

	# test finding an optimal path doesnt go through the floor
	def test_findoptimalpath( self ) :
		for x in range( 100 ):
			self.createOptimalPath()






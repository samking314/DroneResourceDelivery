#
#   testRando.py tests randomly calculated data
#
#   create by: "never go against a sicilian when death is on the line! haha haha haha-...."
#
import unittest
import getRandomData
from random import randint

class MyTest( unittest.TestCase ) :
    def test( self ) :
        test1( self )

def testGetRandoItems( self, numOfItems, XLen, YLen, ZLen ) :
    pointsArr = set()
    pointsArr = getRandomData.getRandomItems( numOfItems, XLen, YLen, ZLen )
    self.assertEqual( len( pointsArr ), numOfItems )

def test1( self ) :
    for x in range( 0, 10 ) :
        testGetRandoItems( self, randint(5, 30), randint(5, 30), randint(5, 30), randint(5, 30) )

def main() :
    unittest.main()

if __name__ == '__main__' :
    main()

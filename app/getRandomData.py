#
#   getRandomData.py returns randomly calculated data
#
#   create by: Samuel King
#

from random import randint

# gets random locations in a field
def createItemLocations( numOfItems, field ) :
	#arr to return
	locationsArr = set()

	i = 0
	while i < numOfItems :
		randomXCoord = randint( 1 , field.xLen - 2 )
		randomYCoord = randint( 1 , field.yLen - 1 )
		randomZCoord = randint( field.fieldFloor[randomXCoord][randomYCoord] , field.zLen - 1 )
		locationsArr.add( ( randomXCoord, randomYCoord, randomZCoord ) )
		i += 1

	return locationsArr

# generates field floor
def createFieldFloor( fieldXLen, fieldYLen, fieldZLen ) :
	#arr to return
	fieldFloorMatrix = [ [ 0 for i in range( fieldXLen ) ] for j in range( fieldYLen ) ]

	i = 0
	j = 0
	while i < fieldXLen :
		while j < fieldYLen :
			#set the max height of ground at 90 meters
			fieldFloorMatrix[i][j] = randint( 0, 90 )
			j += 1
		j = 0
		i += 1

	return fieldFloorMatrix

#
#   getRandomData.py returns randomly calculated data
#
#   create by: Samuel King
#

from random import randint

# creates and returns an item in a field
def createOneItemLocation( field ) :
	location = ( 0, 0, 0 )

	randomXCoord = randint( 1 , field.getxLen() - 2 )
	randomYCoord = randint( 1 , field.getyLen() - 1 )
	fieldFloor = field.getFieldFloor()
	randomZCoord = fieldFloor[randomXCoord][randomYCoord]
	location = ( randomXCoord, randomYCoord, randomZCoord )

	return location

# gets random locations in a field
def createSetOfItemLocations( numOfItems, field ) :
	#arr to return
	locationsArr = set()

	i = 0
	while i < numOfItems :
		randomXCoord = randint( 1 , field.getxLen() - 2 )
		randomYCoord = randint( 1 , field.getyLen() - 1 )
		fieldFloor = field.getFieldFloor()
		randomZCoord = randint( fieldFloor[randomXCoord][randomYCoord] , field.getzLen() - 1 )
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
			#set the max height of ground to half the height of field
			fieldFloorMatrix[i][j] = randint( 0, fieldZLen / 2 )
			j += 1
		j = 0
		i += 1

	return fieldFloorMatrix

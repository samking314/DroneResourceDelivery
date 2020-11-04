#
#   findPath.py finds the optimal path, p
#
#   create by: Samuel King
#

from . import getRandomData, field, timeCosts

class Path ( field.Field ) :

	def __init__ ( self ) :
		super( Path, self ).__init__()
		self.__finalPathString = []
		self.__finalPathCoords = []
		self.__overallTimeCost = 0.0
		self.__zLen = self.getzLen()
		self.__timeCosts = timeCosts.TimeCosts()

	# find opt path, p, s.t. p.overallTimeCost is minimized
	def findOverallPath ( self ) :
		fieldFloor = self.getFieldFloor()
		itemLocations = self.getItemLocations()

		oneItemLocation = itemLocations[0]
		start = ( oneItemLocation[0], oneItemLocation[1], oneItemLocation[2] + 2 )

		# find opt path to item
		pathToItem = self.findPathTrajectoryToItem( fieldFloor, start, False, start, False )

	# Recursively find cost by flipping the graph on its head and traversing it from finish to start.
	# This will allow us to avoid issues of getting stuck behind a 'mountain' and not taking the optimal path.
	def findPathTrajectoryToItem ( self, fieldFloor, startLocation, pickedUp, currCoords, finished ) :
		try :
			self.__finalPathCoords.append( currCoords )

			# return final path
			if finished == True :
				return self.__finalPathString.insert( 0, "Start!" )

			# fist pick up the item
			if startLocation == currCoords and pickedUp == False :
				self.__overallTimeCost += self.__timeCosts.pickupTimeCost
				self.__finalPathString.insert( 0, "Pick up Item from " + str( startLocation ) )
				return self.findPathTrajectoryToItem( fieldFloor, startLocation, True, currCoords, False )

			# can move diagonally
			if currCoords[0] - 1 >= 0 and \
				currCoords[1] - 1 >= 0 and \
				fieldFloor[ currCoords[0] - 1 ][ currCoords[1] - 1 ] < currCoords[2] and \
				fieldFloor[ currCoords[0] - 1 ][ currCoords[1] ] < currCoords[2] and \
				fieldFloor[ currCoords[0] ][ currCoords[1] - 1 ] < currCoords[2] :
				self.__overallTimeCost += self.__timeCosts.moveDiagTimeCost
				nextCoords = ( currCoords[0] - 1, currCoords[1] - 1, currCoords[2] )
				self.__finalPathString.insert( 0, "Move Diagonally from " + str( nextCoords ) )
				fin = nextCoords == ( 0, 0, self.__zLen )
				return self.findPathTrajectoryToItem( fieldFloor, startLocation, True, nextCoords, fin )

			# can move forward
			if currCoords[0] - 1 >= 0 and fieldFloor[ currCoords[0] - 1 ][ currCoords[1] ] < currCoords[2] :
				self.__overallTimeCost += self.__timeCosts.moveForwardTimeCost
				nextCoords = ( currCoords[0] - 1, currCoords[1], currCoords[2] )
				self.__finalPathString.insert( 0, "Move Forward from " + str( nextCoords ) )
				fin = nextCoords == ( 0, 0, self.__zLen )
				return self.findPathTrajectoryToItem( fieldFloor, startLocation, True, nextCoords, fin )
			
			# can move to the right
			if currCoords[1] - 1 >= 0 and fieldFloor[ currCoords[0] ][ currCoords[1] - 1 ] < currCoords[2] :
				self.__overallTimeCost += self.__timeCosts.moveSideTimeCost
				nextCoords = ( currCoords[0], currCoords[1] - 1, currCoords[2] )
				self.__finalPathString.insert( 0, "Move To the Right from " + str( nextCoords ) )
				fin = nextCoords == ( 0, 0, self.__zLen )
				return self.findPathTrajectoryToItem( fieldFloor, startLocation, True, nextCoords, fin )

			# can move down
			if currCoords[2] + 1 <= self.__zLen :
				self.__overallTimeCost += self.__timeCosts.moveDownTimeCost
				nextCoords = ( currCoords[0], currCoords[1], currCoords[2] + 1 )
				self.__finalPathString.insert( 0, "Move Down from " + str( nextCoords ) )
				fin = nextCoords == ( 0, 0, self.__zLen )
				return self.findPathTrajectoryToItem( fieldFloor, startLocation, True, nextCoords, fin )

			raise ValueError("INVALID PATH!")

		except ValueError as e :

			print( "There was an invalid path at " + str(startLocation) + str(pickedUp) + str(currCoords) + str(finished))


	# setter methods

	def changeOverallTimeCost ( self, cost ) :
		self.__overallTimeCost += cost

	def changeTimeCosts (
		self,
		moveDiagTimeCost,
		moveForwardTimeCost,
		moveSideTimeCost,
		moveUpTimeCost,
		moveDownTimeCost,
		pickupTimeCost ) :
		self.__timeCosts.setTimeCosts(
			moveDiagTimeCost,
			moveForwardTimeCost,
			moveSideTimeCost,
			moveUpTimeCost,
			moveDownTimeCost,
			pickupTimeCost
		)

	# getter methods

	def getOverallTimeCost ( self ) :
		return self.__overallTimeCost

	def getFinalPathCoords ( self ) :
		return self.__finalPathCoords

	def getFinalPathString ( self ) :
		return self.__finalPathString






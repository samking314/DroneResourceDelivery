#
#   findPaths.py finds the optimal set of paths P = [ p1, p2, ... , p10 ]
#
#   create by: Samuel King
#

import getRandomData
from random import randint
import datetime


# find the path of each drone recursively

# we need to memoize a 2-dim graph that would contain the sum of the weights of each 
# drone for that step in time












#data points for Drone arrays are ( time, x, y, z )
#the overall unordered set holds Drone arrays called DroneSet

#droneSet contains arrays like {(0,1,2,3),(1,1,3,3),(2,2,3,3)}
droneSet = {}
#openHighways contains arrays like {(1,3,5),(5,8,23),(3,4,5)}
#and these arrays are indexed by the given time t. each arr represents
#all open highways in the factory at a given time t
openHighways = []
#trajectoryArrays contains arrays of trajectories for new Drones
trajectoryArrays = []
#availableDrones is an array of IDs of Drones currently not working
availableDrones = []

#dims of the factory
XLen = 10
YLen = 30
ZLen = 10

exit = ( 10, 30, 0)

MAX_TIME_TO_FINISH = 60 #max time to get item or exit

#TODO: write frunction to take all Drones at given discrete time
#and add a drone to the array of active Drones
def findTrajectory( destination, desiredFinalTime, currentLocation = ( 0, 0, 10 ) ) :
	trajectory = []
	finalTime = desiredFinalTime
	falseFactory = [ [ [ 0 for i in range(0,10)] for j in range(0,30)] for k in range(0,10)]
	while trajectory[ len( trajectory ) ] != currentLocation :
		trajectory = []
		finalTime += 1
		currTime = 0
		falseFactory = recurseTraj( currentLocation, destination, currTime, finalTime, falseFactory )
		#TODO: create func to run the false factory to find truths
	return trajectory

def recurseTraj( currentLocation, destination, currTime, finalTime, falseFactory ) :
	#if there's no way to get there at that time
	if ( len( trajectory ) == 0 and not ( destination in openHighways[finalTime] ) ) :
		return falseFactory
	#WRITE OUT CASES
	#case 1: can't move so just return the same space to the time + space array and recurse again BUT check to see if that space is available
		#case 1.1: if available at that time then stay at the same space to the time + space array and recurse again
		#case 1.2: if the same space isnt available the next time slot then return false and recurse
	#case 2: can move back one space so return the previous space to the t+s array and recurse again
	if ( destination in openHighways[finalTime] ) :
		falseFactory[destination[0]][destination[1]][destination[2]] = 1
		if ( destination[0] == currentLocation[0] and
			destination[1] == currentLocation[1] and
			destination[2] == currentLocation[2] ) :
			return falseFactory
		if ( ( destination[1] & 1 ) == 0 ) :
			return recurseTraj( currentLocation,
								destination,
								currTime,
								finalTime,
								falseFactory )
		else
			return recurseTraj( currentLocation,
								destination,
								currTime,
								finalTime - 1,
								falseFactory )


	if ( len( trajectory ) > 0 and
		( ( destination in openHighways[finalTime] ) or
		( destination in openHighways[finalTime] ) or
		( destination in openHighways[finalTime] )
		) ) :
		falseFactory[destination[0]][destination[1]][destination[2]] = 1
		return recurseTraj( currentLocation,
							destination,
							currTime,
							finalTime - 1,
							falseFactory )


#TODO: write function to continuously update trajectories

#TODO: write function to prevent collisions

#finds a trajectory for drone with new delivery and updates global array data
def newDelivery( numOfItems = 1, pointsArr = [(0,0,10)], currDrones = {}, currHighways = [], currTrajectories = [], currAvailableDrones = [] ) :
	#comment this line out after testing
	pointsArr = getRandomData.getRandomItems( numOfItems, XLen, YLen, ZLen )
	droneSet = currDrones
	openHighways = currHighways
	trajectoryArrays = currTrajectories
	availableDrones = currAvailableDrones
	#figure out trajectory of each drone
	for x in range ( 0, len(pointsArr) ) :
		trajectoryArrays.append(
							findTrajectory(
									pointsArr[x], datetime.datetime.now().time() + MAX_TIME_TO_FINISH
								)
							)
	#return the array of trajectories
	return [ droneSet, openHighways, trajectoryArrays, availableDrones ]

#wherever you are Drone, call me and i will show you the way
def getToExit( currentLocation = ( 0, 0, 10 ) ) :
	return findTrajectory( (XLen, YLen, 0), datetime.datetime.now().time() + MAX_TIME_TO_FINISH )

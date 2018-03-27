#
#   findPaths.py finds the path of all Drones at a given time t
#
#   create by: merry chrystler
#

import getRandomData
from random import randint
import datetime

#data points for Drone arrays are ( time, x, y, z )
#the overall unordered set holds Drone arrays called DroneSet

#droneSet contains arrays like {(0,1,2,3),(1,1,3,3),(2,2,3,3)}
droneSet = {}
#openHighways contains arrays like {(1,3,5),(5,8,23),(3,4,5)}
#and these arrays are indexed by the given time t. each arr represents
#all open highways in the factory at a given time t
openHighways = []
#trajectoryArrays contains arrays of trajectories for new Drones
trejectoryArrays = []
#availableDrones is an array of IDs of Drones currently not working
availableDrones = []

XLen = 10
YLen = 30
ZLen = 10

#TODO: write frunction to take all Drones at given discrete time
#and add a drone to the array of active Drones
def findTrajectory( destination, currTime ) :
    finalTime = currTime #initialize the final time
    #TODO: loop through all time arrays in


#TODO: write function to continuously update trajectories

#TODO: write function to prevent collisions

#TODO: write function to pick up item or to exit
def newDelivery( numOfItems = 1, pointsArr = [(0,0,10)] ) :
    #comment this line out after testing
    pointsArr = getRandomData.getRandomItems( numOfItems, XLen, YLen, ZLen )
    #figure out trajectory of each drone
    for x in range ( 0, len(pointsArr) ) :
        trajectoryArrays.append(
                            findTrajectory(
                                    pointsArr[x], datetime.datetime.now().time()
                                )
                            )
    #return the array of trajectories
    return trajectoryArrays

def getToExit( currentLocation = ( 0, 0, 10) ) :
    #TODO: find the way to the exit
    print("take me out!")

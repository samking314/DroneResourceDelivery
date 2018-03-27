#
#   findPaths.py finds the path of all Drones at a given time t
#
#   create by: merry chrystler
#

from random import randint

#data points for Drone arrays are ( time, x, y, z )
#the overall unordered set holds Drone arrays called DroneSet

#droneSet contains arrays like {(0,1,2,3),(1,1,3,3),(2,2,3,3)}
droneSet = set()
#openHighways contains arrays like {(1,3,5),(5,8,23),(3,4,5)}
#and these arrays are indexed by the given time t. each arr represents
#all open highways in the factory at a given time t
openHighways = array()

#TODO: write frunction to take all Drones at given discrete time
#and add a drone to the array of active Drones
def addDroneToFactory( destination, currTime ) :
    finalTime = currTime
    #TODO: loop through all time arrays in 


#TODO: write function to continuously update trajectories

#TODO: write function to prevent collisions

#TODO: write function to pick up item or to exit

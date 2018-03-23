 DRONE RESOURCE DELIVERY
 
 Problem Statement: Find the number of drones needed in order to remove 10 items placed randomly in the factory in 60 seconds. I.e. you have ten coordinates in the 3-dim space, so find the fastest way to get v1 number of Drones from the entry to their respective shelf locations and all to the exit in 60 seconds.
 
#define the parameters for objects:
# 1. Drones fill a 0.5 cubic meter space.
# 2. Drones travel on average 1 meter per second.
# 2. The factory is a 3-dimensional cube containing 10 x 10 x 30 cubic meters.
# 3. The factory is 10 cubic meters height, 10 cubic meters wide and
#     30 cubic meters long.
# 4. Every odd numbered cubic meter on the y-axis contains a 'shelf' EXCEPT
#     for cubic meters touching the boundary of the factory.
# 5. In total, starting from 0-29, there are 15 'walls' of shelves, so there are
#     15 * 10 = 150 shelves.
# 6. If a cubic meter is not a shelf, it is a transport 'highway' for Drones.
# 7. The coordinates of the first face of the factory are
#     {(0,0,0),(10,0,0),(10,0,10),(10,10,0)} and the second face are
#     {(0,30,0),(0,30,10),(10,30,10),(10,30,0)}.
# 7. The 'entry' point for Drones in the factory is at (0,0,0) and the 'exit' is
#     (10,30,10).
#

#define the parameters for operations:
# 1. Drones enter at the 'entry' point and exit at the 'exit' point.
# 2. Drones are used to enter the 'entry' into the 'highway' of a 3-dimensional
#     factory in order to obtain elements inside of the 'shelves' and move to
#     the 'exit'.
# 3. Drones MUST NOT move beyond the boundary of the factory unless there is
#     and 'entry' or 'exit' point in FRONT or BEHIND them.
# 4. 'move around' is defined as follows:
#       a. A drone can ALWAYS move UP and DOWN.
#       b. IF a drone is A drone can ALWAYS move LEFT and RIGHT ONLY.
#       c. A drone CANNOT move diagonal to its position. (i.e. the Drone's
#         vector MUST NOT have a magnitude greater than 1)
# 5. ONLY ONE Drone can occupy a cubic meter at one time.
# 6. A Drone is either MOVING or STATIONARY. 'moving' and 'stationary' are
#     are defined as follows:
#       a. 'moving' implies a Drone has a non-zero vector inside the
#         3-dim space
#       b. 'stationary' implies a Drone has a zero vector inside the 3-dim space
#

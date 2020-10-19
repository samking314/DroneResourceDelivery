----------------------> DRONE RESOURCE DELIVERY ✈️ 📦

Problem Statement:
	1. Find the number of drones, x, needed and an array of optimal paths, P = [ p1, p2, ..., pw ] (where w doesn't have to be equal to x), in order to remove 10 items placed randomly in the factory from an array of start positions, S = [ s1, s2, ..., sx ], and end positions, E = [ e1, e2, ..., ex ], where S = E. The coordinates are all in a 3-dimensional plane. The drones can only move from 1 cubic meter to the next in straight lines. The drones must avoid ANY possible collisions with obstacles(including other drones). An optimal path, P, decreases the sum of the amount of time it takes for each path, pi, to be completed. The time costs for each movement type are defined below:
		a. moving forward costs 1 second of time
		b. moving to the side costs 1.5 seconds
		c. moving diagonally in any direction costs 2 seconds
		d. stopping is instantaneous and costs no time but waiting can cost any amount of time
	All time costs are based on a step function of either stopping or moving.




// still need to refactor below content

Define the parameters for objects:
	1. Drones fill a 0.5 cubic meter space.
	2. Drones travel on average 1 meter per second.
	3. The factory is a 3-dimensional cube containing 10 x 10 x 30 cubic meters.
	4. The factory is 10 cubic meters height, 10 cubic meters wide and
		30 cubic meters long.
	5. Every odd numbered cubic meter on the y-axis contains a 'shelf' EXCEPT
		for cubic meters touching the boundary of the factory.
	6. In total, starting from 0-29, there are 15 'walls' of shelves, so there are
		15 * 8 = 120 shelves.
 	7. If a cubic meter is not a shelf, it is a transport 'highway' for Drones.
 	8. The coordinates of the first face of the factory are
		{(0,0,0),(10,0,0),(10,0,10),(10,10,0)} and the second face are
		{(0,30,0),(0,30,10),(10,30,10),(10,30,0)}.
 	9. The 'entry' point for Drones in the factory is at (0,0,10) and the 'exit' is
		(10,30,0). (the drones start at top since they use less power traveling
		down than they do up)
 	10. The factory items all face in one direction. I.e., if all the items face
		negative y-axis then an item in row x is only accessible from row x - 1.
		This makes sense considering there is no 'aisle 30' so items in shelf 29
		would not be accessible if they faced the positive y-axis


Define the parameters for operations:
	1. Drones enter at the 'entry' point and exit at the 'exit' point.
	2. Drones are used to enter the 'entry' into the 'highway' of a 3-dimensional
		factory in order to obtain elements inside of the 'shelves' and move to
		the 'exit'.
	3. Drones MUST NOT move beyond the boundary of the factory unless there is
		an 'entry' or 'exit' point in FRONT or BEHIND them.
	4. 'move around' is defined as follows:
		a. A drone can ALWAYS move UP and DOWN.
		b. IF a drone is not on a boundary it can ALWAYS move LEFT and RIGHT.
		c. A drone CANNOT move diagonal to its position. (i.e. the Drone's
			vector MUST NOT have a magnitude greater than 1)
	5. ONLY ONE Drone can occupy a cubic meter at one time.
	6. A Drone is either MOVING or STATIONARY. 'moving' and 'stationary' are
		are defined as follows:
			a. 'moving' implies a Drone has a non-zero vector inside the
				3-dim space
			b. 'stationary' implies a Drone has a zero vector inside the 3-dim space

DRONE RESOURCE DELIVERY ✈️ 📦

Problem Statement:
	Find the optimal set of paths, p, in order to remove 1 item placed randomly in the field at position s. The coordinates are all in a 3-dimensional plane. An optimal path, p, decreases the sum of the amount of time it takes for p to be traversed by the drone.

Define the parameters for objects:
	1. A drone fills a 0.5 cubic meter space.
	2. The field is a 3-dimensional cube containing 100 cubic meters.
 	3. If a cubic meter is not an obstacle, it is a transport 'highway' for a drone.
 	4. The coordinates of the first face of the field are
		{(0,0,0),(100,0,0),(100,0,100),(0,0,100)} and the second face are
		{(0,100,0),(0,100,100),(100,100,100),(100,100,0)}.
 	5. The 'entry' point for a drone in the field is at (0,0,100) and the 'exit' is
		the top line of cubes from (100,100,100) to (0,100,100).

Define the parameters for operations:
	1. A drone must enter at the 'entry' point and exit at any of the 'exit' points.
	2. A drone MUST NOT move beyond the boundary of the field unless there is
		an 'entry' or 'exit' point in FRONT or BEHIND it.
	3. The time costs for each movement type are defined below:
		a. moving forward 1 meter costs 1.0 second of time
		b. moving to the side 1 meter costs 1.25 seconds
		c. moving diagonally in any direction 1 meter costs 2.0 seconds
		d. stopping is instantaneous and costs no time but waiting can cost any amount of time
		e. picking up an item once stopped takes 12.0 seconds
		All time costs are based on a step function of either stopping or moving.
	4. A Drone is either MOVING or STATIONARY. 'moving' and 'stationary' are
		are defined as follows:
			a. 'moving' implies a Drone has a non-zero vector inside the
				3-dim space
			b. 'stationary' implies a Drone has a zero vector inside the 3-dim space
	5. A drone can only move from 1 cubic meter to the next in straight lines.
	6. A drone must avoid ANY possible collisions with obstacles.
	7. Finally, a drone can pick up an item from any height below or at 10 meters high
		from the height of the field floor at that location.

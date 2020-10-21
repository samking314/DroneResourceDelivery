DRONE RESOURCE DELIVERY ✈️ 📦

Problem Statement:
	Find the optimal set of paths, P = [ p1, p2, ..., p10 ], in order to remove 10 items placed randomly in the field at an array of positions, S = [ s1, s2, ..., s10 ]. The coordinates are all in a 3-dimensional plane. An optimal set of paths, P, decreases the sum of the amount of time it takes for each path, pi in P, to be completed.

Define the parameters for objects:
	1. Drones fill a 0.5 cubic meter space.
	2. The field is a 3-dimensional cube containing 100 cubic meters.
 	3. If a cubic meter is not an obstacle, it is a transport 'highway' for Drones.
 	4. The coordinates of the first face of the field are
		{(0,0,0),(100,0,0),(100,0,100),(0,0,100)} and the second face are
		{(0,100,0),(0,100,100),(100,100,100),(100,100,0)}.
 	5. The 'entry' point for Drones in the field is at (0,0,100) and the 'exit' is
		the top line of cubes from (100,100,100) to (0,100,100).

Define the parameters for operations:
	1. Drones enter at the 'entry' point and exit at the 'exit' points.
	2. Drones MUST NOT move beyond the boundary of the field unless there is
		an 'entry' or 'exit' point in FRONT or BEHIND them.
	3. The time costs for each movement type are defined below:
		a. moving forward 1 meter costs 1.0 second of time
		b. moving to the side 1 meter costs 1.25 seconds
		c. moving diagonally in any direction 1 meter costs 2.0 seconds
		d. stopping is instantaneous and costs no time but waiting can cost any amount of time
		e. picking up an item once stopped takes 12.0 seconds
		All time costs are based on a step function of either stopping or moving.
	4. ONLY ONE Drone can occupy a cubic meter at one time.
	5. A Drone is either MOVING or STATIONARY. 'moving' and 'stationary' are
		are defined as follows:
			a. 'moving' implies a Drone has a non-zero vector inside the
				3-dim space
			b. 'stationary' implies a Drone has a zero vector inside the 3-dim space
	6. The drones can only move from 1 cubic meter to the next in straight lines.
	7. The drones must avoid ANY possible collisions with obstacles (including other drones).
	9. A drone must ONLY pick up 1 item, anymore and it will crash!
	10. Finally, drones can pick up an item from any height below or at 10 meters high.

## Welcome to The Drone Resource Repo!

Here you can test and simulate a drone delivering an item to a specified location given a defined field with boundaries and obstacles.



The path found using my recursive algorithm is indeed optimal. The funny thing is, I flipped 
the graph upside down and start the drone at it's final destination and then work backward from there to find the optimal path. 
I could've used the algorithm the right side up but then would've had to memoize the entire path trajectories which is O(n^3) and
then had to check all paths inside the memoized matrix to find the optimal path which would've been O(n^2) <- I could be wrong here if you
find a clever way to search all paths.

Regardless, I cut the complexity of both computation and search to O(1) and O(1) with the upside down trick I mentioned before.

If you have any questions at all please reach out! (email's in my bio)

## to run
```
make deploy
```

## to test
```
make test
```

## if failing
```
rm -rf .venv
make deploy
```

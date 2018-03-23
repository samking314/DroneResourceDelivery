from random import randint

def getRandomItems( numOfItems, factXLen, factYLen, factZLen ) :
    #arr to return
    pointsArr = set()

    while len( pointsArr ) < numOfItems :
        #using 0-14 since only odd ailes have shelves
        point = ( randint(1,factXLen - 2), randint(0,factYLen - 1), randint(0,factZLen - 1) )
        print(point[1] & 1)
        if ( point[1] & 1 ) == 0 :
            newPoint = point[1] + 1
            point = ( point[0], newPoint, point[2] )
        #point = ( point[0], point[1] * 2, point[2])
        pointsArr.add( point )

    return pointsArr


print(getRandomItems(5,10,30,10))

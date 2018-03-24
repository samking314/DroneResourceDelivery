
#
#   getRandomData.py returns randomly calculated data
#
#   create by: ohmahgod he on xgames
#


from random import randint

def getRandomItems( numOfItems, factXLen, factYLen, factZLen ) :
    #arr to return
    pointsArr = set()

    while len( pointsArr ) < numOfItems :
        #using 1...factXlen-2 since the first and last rows are 'highways'
        point = ( randint(1,factXLen - 2), randint(0,factYLen - 1), randint(0,factZLen - 1) )

        if ( point[1] & 1 ) == 0 :
            newPoint = point[1] + 1
            point = ( point[0], newPoint, point[2] )

        pointsArr.add( point )

    return pointsArr

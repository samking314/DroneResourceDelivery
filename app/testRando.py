import unittest

#import sys
#sys.path.append('/Users/samking/PythonProjects/DroneResourceRepo/app/getRandomData.py')
#import file
import getRandomData
#getRandomData = input('getRandomData:')
#importlib.import_module(getRandomData)

#def fun(x):
#    return x + 1

class MyTest(unittest.TestCase):
    def test(self):
        pointsArr = set()
        pointsArr = getRandomData.getRandomItems(10,10,30,10)
        self.assertEqual(len(pointsArr), 10)

def main():
    unittest.main()

if __name__ == '__main__':
    main()

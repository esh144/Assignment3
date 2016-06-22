#input 2 coordinates and calculate the distance between the two points
import math


def DistanceFormula(x1, y1, x2, y2):
    end = False
    
    try:
        val = int(x1)
        val2 = int(y1)
        val3 = int(x2)
        val4 = int(y2)
    except ValueError:
        print ("Invalid Input")
        distance = "Invalid Input"
        end = True
    if (end == True):
        return distance
    
    first = (x2 - x1)
    second = (y2 - y1)
    first = pow(first, 2)
    second = pow(second, 2)
    distance = math.sqrt(first + second)
    return distance

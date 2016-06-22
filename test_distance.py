#Test the Distance Formula application
from distanceformula import *

def test_1():
    x1 = 5
    y1 = 3
    x2 = 10
    y2 = 15
    assert DistanceFormula(x1, y1, x2, y2) == 13

def test_2():
    x1 = 10
    y1 = 15
    x2 = 5
    y2 = 3
    assert DistanceFormula(x1, y1, x2, y2) == 13

def test_3():
    x1 = "!"
    y1 = 9
    x2 = 4
    y2 = 15
    assert DistanceFormula(x1, y1, x2, y2) == "Invalid Input"

def test_4():
    x1 = -8
    y1 = -9
    x2 = -5
    y2 = -7
    assert DistanceFormula(x1, y1, x2, y2) == math.sqrt(13)

def test_5():
    x1 = 56
    y1 = 67
    x2 = 878
    y2 = 453
    assert DistanceFormula(x1, y1, x2, y2) != 8

def test_6():
    x1 = 56
    y1 = 67
    x2 = 878
    y2 = 453
    assert DistanceFormula(x1, y1, x2, y2) == math.sqrt(824680)


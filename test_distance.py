#Test the Distance Formula application
from distanceformula1 import *

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

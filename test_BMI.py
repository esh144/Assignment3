# Test BMI function

from bmi import *

def test_BMI():
    height_feet = 5
    height_inches = 3
    weight_lbs = 125

    assert BMI(height_feet, height_inches, weight_lbs) == "Normalweight"


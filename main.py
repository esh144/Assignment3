# Main Program

#Include BMI function file
from bmi import *

#Include Retirement function file

#Include Distance formula file
from distanceformula import *

print("Function Menu")
print("-------------")
print("1.) Body Mass Index")
print("2.) Retirement")
print("3.) Distance Formula")
print("0.) Quit")
print('')
function_choice = int(input("Function choice: "))
while function_choice != 0:
    if function_choice == 1:
        feet = int(input("Enter height as a integer: "))
        inches = int(input("Enter remaining height in inches: "))
        weight = int(input("Enter weight in pounds: "))
        result = BMI(feet, inches, weight)
        print("BMI Result: You are ", result)
                 
    if function_choice == 3:
        x1 = int(input("Enter the x value of the first value pair: "))
        y1 = int(input("Enter the y value of the first value pair: "))
        x2 = int(input("Enter the x value of the second value pair: "))
        y2 = int(input("Enter the y value of the second value pair: "))
        result = DistanceFormula(x1, y1, x2, y2)
        if (result != "Invalid Input"):
            result = "{0:.2f}".format(result)
            print("The distance between the two points is ", result)

    print("")
    function_choice = int(input("Enter another function choice: "))


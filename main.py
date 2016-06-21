# Main Program

#Include BMI function file
from bmi import *

#Include Retirement function file

#Include Distance formula file

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
                 



    print("")
    function_choice = int(input("Enter another function choice: "))


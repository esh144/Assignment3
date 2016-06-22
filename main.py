# Main Program

#Include BMI function file
from bmi import *

#Include Retirement function file
from retire import *

#Include Distance formula file


loop = True

print("Function Menu")
print("-------------")
print("1.) Body Mass Index")
print("2.) Retirement")
print("3.) Distance Formula")
print("0.) Quit")
print('')

while loop == True:
    try:
        function_choice = int(input("Enter valid Function choice: "))
    except:
        print("Enter valid choice")
    else:
        if function_choice == 1:
            print("")
            print("Body Mass Index")
            print("---------------")
            feet = int(input("Enter height in feet (as a integer): "))
            inches = int(input("Enter remaining height in inches (as an integer): "))
            weight = int(input("Enter weight in pounds: "))
            result = BMI(feet, inches, weight)
            print("BMI Result: You are ", result)
            print("")
        
        elif function_choice == 2:
            age = int(input("Enter your current age: "))
            annual_sal = int(input("Enter your annual salary: "))
            percentage = int(input("Enter the percent you wish to save from your annual salary (integer only):"))
            goal = int(input("What is your desired goal for your retirement savings?"))
            result = calucate_years_to_goal (age, annual_sal, percentage, goal)
            print(result)

        elif function_choice == 0:
            print("Program ended.")
            break

            
            



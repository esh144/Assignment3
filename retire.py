import math

def calucate_years_to_goal (age, annual_sal, percentage, goal):
	putback = (percentage/100) * annual_sal* 2
	years = goal/putback
	age_to_goal = years + age
	age_to_goal = math.floor(age_to_goal)
	
	if age_to_goal >= 100:
		print("You will be", age_to_goal, "years old")
		return "Goal will not be reached in a lifetime"
	else:
		print ("Your age when goal is reached:")
		return  age_to_goal

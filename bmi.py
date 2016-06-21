# Body Mass Index Function 

def BMI(height, inches, weight):
    weight_kg = weight * 0.45
    height_in = height * 12
    height_m = (height_in + inches) * 0.025
    answer = height_m * height_m
    bmi = weight_kg / answer
    print(bmi)

    if bmi <= 18.5:
        return "Underweight"
    if bmi > 18.5 and bmi <= 24.9:
        return "Normalweight"
    if bmi >= 25 and bmi <= 29.9:
        return "Overweight"
    else:
        return "Obesity"

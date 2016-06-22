# Body Mass Index Function 

def BMI(height, inches, weight):
    try:
        height = int(height)
        inches = int(inches)
        weight = int (weight)
        
        
    except:
        result = "invalid"
    
    else: 
        weight_kg = weight * 0.45
        height_in = height * 12
        height_m = (height_in + inches) * 0.025
                  
        answer = height_m * height_m
        bmi = weight_kg / answer
        print("BMI: ", bmi)

        if bmi <= 18.5:
            result = "Underweight"
        elif bmi > 18.5 and bmi <= 24.9:
            result = "Normalweight"
        elif bmi >= 25 and bmi <= 29.9:
            result = "Overweight"
        else:
            result = "Obesity"

    return result

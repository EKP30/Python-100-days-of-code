height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
BMI_number = weight / (height * height)
BMI_number = round(BMI_number)
if BMI_number < 18.5:
    print(f"Your BMI is {BMI_number}, you are underweight.")
elif BMI_number < 25:
    print(f"Your BMI is {BMI_number}, you have a normal weight.")
elif BMI_number < 30:
    print(f"Your BMI is {BMI_number}, you are slightly overweight.")
elif BMI_number < 35:
    print(f"Your BMI is {BMI_number}, you are obese.")
elif BMI_number >= 35:
    print(f"Your BMI is {BMI_number}, you are clinically obese.")
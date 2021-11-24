def bmi_script_5(height, weight):
     bmi = 2* height*weight
     return "Your BMI is {} which means you are obese.".format(bmi)

if __name__ == '__main__':
    name = input("What is your Name:")
    height = float(input("What is your Height in metres?"))
    weight = int(input("What is your Weight in Kg?"))
    
    bmi_script_5(height, weight)
BMI = round(weight/ (height * height), 1)
print(f"Your BMI is {BMI}")

if BMI < 18.5:
    print(f"Your BMI is {BMI} which means you are underweight.")
elif BMI >18.5 or BMI <= 24.9:
    print(f"Your BMI is {BMI} which means you are normal.")
elif BMI >24.9 or BMI <= 29.9:
    print(f"Your BMI is {BMI} which means you are over weight.")
elif BMI >= 30.0:
    print(f"Your BMI is {BMI} which means you are obese.")
else:
    print(f"Your BMI is {BMI} which means you are severely obese.")

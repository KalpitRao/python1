def bmi_script_5(height, weight):
     bmi = 2* height*weight
     return ('Your BMI is {bmi} which means you are obese.'.format(bmi))

if __name__ == '__main__':
     name = input("What is your Name:")
     height = float(input("Hi "+name +" What is your Height in metres?"))
     weight = int(input("What is your Weight in Kg?"))
     bmi_script_5(height, weight)

if bmi <= 18.5:
    print("You are underweight.")
elif bmi <= 24.9:
    print("You are normal.")
elif bmi <= 29.9:
    print("You are over weight.")
elif bmi >= 30.0:
    print("You are obese.")
else:
    print("You are severely obese.")



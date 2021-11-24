"""
name=input("Whats your name")
print("hie"    +name)
age=input("Whats your age ?")
print(age)
weight=input("Whats your weight in kg?")
print(weight)

height=input("Whats your height in metres?")
print(height)

"""



def bmi_script_4(age,height, weight):
     return ""

if __name__ == '__main__':
     age= int(input("Hi Argo, What is your Age?"))
     height = float(input("What is your Height in metres?"))
     weight = int(input("What is your Weight in Kg?"))
    
     bmi_script_4(age,height, weight,)

BMI = round(weight/ (height * height), 1)
print(f"You BMI is {BMI}")
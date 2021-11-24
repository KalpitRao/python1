import sys

def bmi_script_5(height, weight):
     bmi = 2* height*weight
     return "Your BMI is {} which means you are obese.".format(bmi)

     if bmi < 18.5:
      return "Your Bmi is {} which means you are underweight.".format(bmi)
     elif bmi < 24.9:
      return "Your Bmi is {} which means you are Normal.".format(bmi)    
     elif bmi < 29.9:
      return "Your Bmi is {} which means you are Overweight.".format(bmi)    

     else: 
      return "Your Bmi is {} which means you are obese.".format(bmi)    

if __name__ == '__main__':
    name=sys.argv[1]
    height = float(sys.argv[2])
    weight = int(sys.argv[3])
    print(f'Name:{name}')
    print(f'Height:{height}')
    print(f'Weight:{weight}')
    print(bmi_script_5(height,weight))
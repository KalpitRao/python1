#print("Hello Python")
#print("hie")



#name= input("Whats Your Name?")
#print(name)

#print("hjefylhjfkhnkrd")

number1=3
number2=4
number3=5
print(f'{number1} times {number2}times{number3}')

var_list=list(range(0,100,7))
print(var_list)


for i in range(100):
    print(i)


for y in var_list:
    print(y+1)



list=["kalpit","gomiJio","Rao"]
for i in list:
    print(i+ "*") 

if 1>5:
    print("yes")
elif 3>8:
    print("yes")    
elif 4>8:
    print("yes") 
else:
    print("No")       



"""
students_marks=range(0,99)

for i in students_marks:
    marks=int(input("Enter Your marks?"))
    if i==35 or i<40:
        print("Just passed with")
    elif i>=50 or i<74:
        print("Average marks with")
    elif i>=75 or i<89:
        print("Good marks with")
    elif i>90 or i<=98:
        print("Excellent marks with")
    else:
        print("Failed")


"""

def myfunc(text):
    print("Welcome to " + text)
myfunc("INdia")    


def teams(team="SRH"):
    print("I Play for "+ team)
teams("Delhi")      

numbers = [1,2,3,4,5]
Weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday','Friday','Saturday','Sunday']
Num = [222,100,85,500,300]

for i in numbers:
    print(i)

i=1
while 1<6:
    print(i)
    if i ==5:
        break
    i+=1    

for i in Weekdays:
    print(i)


days = 0
while days < 7:
    print(Weekdays)
    break
days += 1
                  
sum = 0
for x in Num:
      sum = sum + x

print("The sum from for loop",sum)

sum=0
list_size = len(Num)
loop_counter = 0
while loop_counter < list_size:
    sum = sum + Num[loop_counter]
    loop_counter = loop_counter + 1
print("The sum from while loop", sum)
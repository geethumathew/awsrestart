# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
#number=input("enter the number")
#number=int(number)  # Convert the user input to an integer


c=[2200,2350,2600,2130,2190]
for i in range(0,1):
        result=c[i+1]-c[i]
print(result)


sum=0
for i in range(0,3):
        sum=sum+c[i]
print(sum)


value=2000
found = False
for i in range(len(c)):
    if(value==c[i]):
       found = True
       break
if(found):
     print("value is 2000")
else:
    print("not found")
    
    
junevalue =1980    
c.append(junevalue)
print(c)

for i in range(c[-2]):
    c[i]=c[i]-200
print(c[i])

    
    
    
    
    
    
    
        
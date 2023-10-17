months = ["January", "February", "March", "April", "May"] 
expenses = [2200,2350,2600,2130,2190]
combinedlist = []

for i in range(len(expenses)):
    combinedlist.append((months[i],expenses[i]))
    
print(combinedlist)
    
dir(combinedlist)

    
   
junetuple = ("june",1980)   
combinedlist.append(junetuple)
print(combinedlist)




myFruitList = ["apple", "banana", "cherry"]
""" 
#print(myFruitList)
#myFruitList.append("strwaberry")
#myFruitList.insert(2,"banana")
#print(myFruitList)
myFruitList.remove("banana")
print(myFruitList)
list2=["banana","apple"]
myFruitList.extend(list2)
print(myFruitList)
myFruitList = ("apple", "banana", "cherry")
print(myFruitList[0])
new =(1,2,3)
print(myFruitList,new,new)
a=dir(new)
print(a)
print(new.index(1))

myMixedTypeList = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}

#print(myFavoriteFruitDictionary["Akua"])

#print(myFavoriteFruitDictionary)
b = {'name':['sam','mark','steve'],'age':[21,21,22]}
print(b)

for x in range(6):
    print(x)

for name, fruit in b.items():
    print("{} likes {}".format(name, fruit))
    
a=[{'id':'emp1','sal':1000},{'id':'emp2','sal':1500}]
print(a[0]['id'])
    
for item in a:
    print(item['id'], item['sal'])
 """   
    
    
    
 a=[25,10,32,65,[34,45,32]]
print(a[-1])
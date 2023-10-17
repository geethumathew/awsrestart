def print_stock_info(myFavoriteFruitDictionary):
    for key, value in myFavoriteFruitDictionary.items():
        print(value)
        avearge=0
        for i in range(len(value)):
            avearge=avearge+value[i]/2
        print("{}==> {} avg:==>{}".format(key,value,avearge))
def print_stock_add(myFavoriteFruitDictionary):
    key = input("Enter a key: ")
    value = int(input("Enter a value: ")) 
    if key in myFavoriteFruitDictionary:
        myFavoriteFruitDictionary[key].append(value)
    else:
        myFavoriteFruitDictionary[key] = [value]
    print(myFavoriteFruitDictionary)
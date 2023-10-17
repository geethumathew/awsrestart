import Ticketbookingvalues as mm
username = input("Enter username : ")
print("greeting {} !!!!".format(username))
print("plese find the movie list {}".format(mm.movieslist))
movie=input("select a movie 1/2/3:")
moviename = mm.movieslist[movie]
print("you have selected {}".format(mm.movieslist[movie]))
print("plese find the price list {}".format(mm.pricelistmovie))
selectprice=input("select a movie circle:")
ticket=int(input("Number of tickets:"))
required = input("is food required : ")
combo="no combo selected "
combonumber=0
if required=="yes":
    print("please find the food list {}".format(mm.combolist))
    print("please find the price list {}".format(mm.pricelist))
    combo = input("select the  combos :")
    print("you have selected {}".format(combo))
    combonumber = int(input("select the number of combos :"))
    foodprice=mm.calculateprice(combo,combonumber)
    totalprice=mm.calculatetotalprice(ticket,selectprice,foodprice)
elif required == "no":
    print("continue your purchase")
    totalprice=mm.pricelistmovie[selectprice]
print("your total price is {}".format(totalprice))
putputlist=mm.addtoemptydictionary(username,moviename,ticket,combo,combonumber)
print(putputlist)
f = open("./mytext.txt", "a")
f.write(str(putputlist))
f.close()

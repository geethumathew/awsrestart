

movieslist= {
  "1" : "titanic",
  "2" : "godzilla",
  "3" : "juraric park"
}
pricelistmovie= {
  "silver" : 100,
  "gold" : 200,
  "platinum": 300
}

combolist= {
  "combo1" : ["pizza","coke","fries"],
  "combo2" : ["burger","coke","fries"],
  "combo3" : ["noodels","bubletea"]
}

pricelist= {
  "combo1" :  5,
  "combo2" :  6,
  "combo3" :  7
}


userlist={}

def calculateprice(combo,combonumber):
  if combo =="combo1":
    comboprice=combonumber*pricelist["combo1"]
  if combo =="combo2":
    comboprice=combonumber*pricelist["combo2"]
  if combo =="combo3":
    comboprice=combonumber*pricelist["combo3"]
  return comboprice

def calculatetotalprice(ticket,selectprice,foodprice):
  return ticket*pricelistmovie[selectprice]+foodprice
  
def addtoemptydictionary(username,movie,ticket,combo,combonumber):
  listnew={movie:ticket},{combonumber,combo}
  userlist[username]=listnew
  return userlist
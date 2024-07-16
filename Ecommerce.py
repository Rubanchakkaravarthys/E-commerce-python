print("\t\t\t\t\t Online Shopping")
print()
print("-----------------------------------------------------------------------"*2)
print()
print("Product List")
print("------------------------------------------------------------------------"*2)
print()
print("1.Mobiles\t2.Tv\t3.Laptop\t4.Tab")
user = input("pick up any one :")
print("------------------------------------------------------------------------"*2)
print()
productlist = ("mobiles")
productlist1 =("tv")
productlist2 = ("laptop")
productlist3 = ("tab")
if user.lower()==productlist:
    print("1.Apple\t2.Samsung\t3.Vivo\t4.Nothing")
elif user.lower()==productlist1:
    print("1.Sony\t2.Samsung\t3.LG\t4.Panasonic")
elif user.lower()==productlist2:
    print("1.Imac\t2.Hp\t3.Lenovo\t4.Dell")
elif user.lower()==productlist3:
    print("1.Oppo\t2.Ipad\t3.Honor\t4.Huawei")
else:
    print("There is a no productlist")
print()
user = input("pick up any one :")
print("------------------------------------------------------------------------"*2)
dict ={
    "apple":{
        "brandname":"iphone",
        "model"    :"iphone15",
        "price"    : 74000,
    },
    "samsung":{
        "brandname":"samsung",
        "model"    :"samsung23ultra",
        "price"    :125000,
    },
    "vivo":{
        "brandname":"vivo",
        "model"    :"vivo t2x",
        "price"    :15000,
    },
    "nothing":{
        "brandname":"nothing",
        "model"    :"nothing 2a",
        "price"    :24000,
    },
    "sony":{
        "brandname":"sony",
        "model"    :"sonykd",
        "price"    :80000 ,
    },
    "samsung":{
        "brandname":"samsung",
        "model"    :"samsungCUE70",
        "price"    : 31000 ,
    },
    "lg":{
        "brandname":"lg",
        "model"    :"lg ultra",
        "price"    : 139910 ,
    },
    "panasonic":{
        "brandname":"panasonic",
        "model"    :"panasonic LED",
        "price"    : 20000 ,
    },
    "imac":{
        "brandname":"apple",
        "model"    :"macbook air m1",
        "price"    :112490 ,
    },
    "hp":{
        "brandname":"hp",
        "model"    :"hp victus",
        "price"    :65000 ,
    },
    "lenovo":{
        "brandname":"lenovo",
        "model"    :"thinkpad E16",
        "price"    :70991  ,
    },
    "dell":{
        "brandname":"dell",
        "model"    :"dell inspiron",
        "price"    :47990  ,
    },
    "oppo":{
        "brandname":"oppo",
        "model"    :"pad airtablet",
        "price"    : 11000  ,
    },
    "ipad":{
        "brandname":"ipad",
        "model"    :"ipad air",
        "price"    : 58000 ,
    },
    "honor":{
        "brandname":"honor",
        "model"    :"honor pad8",
        "price"    :15000  ,
    },
    "huawei":{
        "brandname":"huawei",
        "model"    :"mediapad t1",
        "price"    : 6899   ,
    }

}
if user in dict:
    brandname = dict[user] ["brandname"]
    model     = dict[user] ["model"]
    price     = dict[user] ["price"]
    print("Brandname :",brandname)
    print("Model :",model)
    print("Price :",price)
elif user in dict:
    brandname1 = dict[user] ["brandname"]
    model1     = dict[user] ["model"]
    price1    = dict[user] ["price"]
    print("Brandname :",brandname1)
    print("Model :",model1)
    print("Price :",price1)
elif user in dict:
    brandname2 = dict[user] ["brandname"]
    model2     = dict[user] ["model"]
    price2     = dict[user] ["price"]
    print("Brandname :",brandname2)
    print("Model :",model2)
    print("Price :",price2)
elif user in dict:
    brandname3 = dict[user] ["brandname"]
    model3     = dict[user] ["model"]
    price3     = dict[user] ["price"]
    print("Brandname :",brandname3)
    print("Model :",model3)
    print("Price :",price3)
elif user in dict:
    brandname4 = dict[user] ["brandname"]
    model4     = dict[user] ["model"]
    price4     = dict[user] ["price"]
    print("Brandname :",brandname4)
    print("Model :",model4)
    print("Price :",price4)
elif user in dict:
    brandname5 = dict[user] ["brandname"]
    model5     = dict[user] ["model"]
    price5     = dict[user] ["price"]
    print("Brandname :",brandname5)
    print("Model :",model5)
    print("Price :",price5)
elif user in dict:
    brandname6 = dict[user] ["brandname"]
    model6     = dict[user] ["model"]
    price6     = dict[user] ["price"]
    print("Brandname :",brandname6)
    print("Model :",model6)
    print("Price :",price6)
elif user in dict:
    brandname7 = dict[user] ["brandname"]
    model7     = dict[user] ["model"]
    price7     = dict[user] ["price"]
    print("Brandname :",brandname7)
    print("Model :",model7)
    print("Price :",price7)
elif user in dict:
    brandname8 = dict[user] ["brandname"]
    model8     = dict[user] ["model"]
    price8     = dict[user] ["price"]
    print("Brandname :",brandname8)
    print("Model :",model8)
    print("Price :",price8)
elif user in dict:
    brandname9 = dict[user] ["brandname"]
    model9     = dict[user] ["model"]
    price9     = dict[user] ["price"]
    print("Brandname :",brandname9)
    print("Model :",model9)
    print("Price :",price9)
elif user in dict:
    brandname10 = dict[user] ["brandname"]
    model10     = dict[user] ["model"]
    price10     = dict[user] ["price"]
    print("Brandname :",brandname10)
    print("Model :",model10)
    print("Price :",price10)
elif user in dict:
    brandname11 = dict[user] ["brandname"]
    model11     = dict[user] ["model"]
    price11    = dict[user] ["price"]
    print("Brandname :",brandname11)
    print("Model :",model11)
    print("Price :",price11)
elif user in dict:
    brandname12 = dict[user] ["brandname"]
    model12     = dict[user] ["model"]
    price12     = dict[user] ["price"]
    print("Brandname :",brandname12)
    print("Model :",model12)
    print("Price :",price12)
elif user in dict:
    brandname13 = dict[user] ["brandname"]
    model13     = dict[user] ["model"]
    price13     = dict[user] ["price"]
    print("Brandname :",brandname13)
    print("Model :",model13)
    print("Price :",price13)
elif user in dict:
    brandname14 = dict[user] ["brandname"]
    model14    = dict[user] ["model"]
    price14     = dict[user] ["price"]
    print("Brandname :",brandname14)
    print("Model :",model14)
    print("Price :",price14)
elif user in dict:
    brandname15 = dict[user] ["brandname"]
    model15    = dict[user] ["model"]
    price15     = dict[user] ["price"]
    print("Brandname :",brandname15)
    print("Model :",model15)
    print("Price :",price15)
else:
    print("There is a no information found")
print()
user = input("pick up yes or no:")
print("------------------------------------------------------------------------"*2)
# no=exit()
name=input("Enter your name :")
mobileno=int(input("Enter a mobileno :"))
address = input("Enter your address :")
quantity = int(input("Enter a quantity :"))
quantity_price_concate = int(price)*quantity

print("------------------------------------------------------------------------"*2)
if user.lower()=="yes":
    print("\n","Name :",name,"\n","Mobileno :",mobileno,"\n","Address :",address,"\n","Quantity :",quantity)
else:
    print("invalid input !!!")
print()
print("------------------------------------------------------------------------"*2)
print("Name\t\tMobileno\t\tAddress\t\t\t\t\tQuantity\t\tPrice")
print(name,"\t\t",mobileno,"\t\t",address,"\t\t",quantity,"\t\t\t",quantity_price_concate)

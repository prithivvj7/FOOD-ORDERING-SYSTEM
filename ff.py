from tabulate import tabulate
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    username="root",
    passwd="Admin@12345",
    database="online_order"
    )
if mydb.is_connected():
    print("connection established")
mycursor=mydb.cursor()
    
def payment():
    print("your customer id is",idl)
    print("grand total :",total)
    print("enter your card number")
    cardno=int(input())
    if cardno==123456:
        print("valid card no")
    elif cardno==789123:
        print("valid user")
    elif cardno==456789:
        print("valid user")
    elif cardno==112345:
        print("valid user")
    elif cardno==678901:
        print("valid user")
    elif cardno==234567:
        print("valid user")
    elif cardno==890123:
        print("valid user")
    elif cardno==135792:
        print("valid user")
    else :
        print ("invalid card number")
        return payment()
    print("enter your pin")
    pin=int(input())
    if pin==1234:
        print("your order is placed")
        return billing()
    elif pin==5678:
        print("your order is placed")
        return billing()
    elif pin==9012:
        print("your order is placed")
        return billing()
    elif pin==3456:
        print("your order is placed")
        return billing()
    elif pin==7890:
        print("your order is placed")
        return billing()
    elif pin==1357:
        print("your order is placed")
        return billing()
    elif pin==2468:
        print("your order is placed")
        return billing()
    elif pin==1157:
        print("your order is placed")
        return billing()
    else :
        print("invalid pin")
        return payment()
 
def billing():
    bid= int(input("Enter your registered customer id"))
    tamnt=print("total amount",total)
    paid=print("paid")
    
    
def orders():
    print(tabulate ([["MENU ID","ITEMS","PRICE"],["MENU ID 1","BRIYANI","150"],["MENU ID 2","PAROTTA","15"],["MENU ID 3","CHAPPATI",15],["MENU ID 4","NOODLES",130],["MENU ID 5","FRIEDRICE",130],["MENU ID 6","MEALS",150],["MENU ID 7","ICECREAM",60],["MENU ID 8","LEMONADE",30],["MENU ID 9","BROWNIE",80],["MENU ID 10","JAMUN",45],["exit 0"],["to place order 11"]],headers="firstrow"))
    opt=int(input("select your delicious food number"))
    global total
    if opt==1:
        price=150
        d=int(input("enter the  quantity"))
        total+=price*d
        print("subtotal- ",total)
        return orders()
    elif opt==2:
        price=15
        d=int(input("enter the  quantity"))
        total+=price*d
        print("subtotal-",total)
        return orders()
    elif opt==3:
        price=15
        d=int(input("enter the  quantity"))
        total+=price*d
        print("subtotal -",total)
        return orders()
    elif opt==4:
        price=130
        d=int(input("enter the  quantity"))
        total+=price*d
        print("subtotal-",total)
        return orders()
    elif opt==5:
        price=130
        d=int(input("enter the  quantity"))
        total+=price*d
        print("subtotal-",total)
        return orders()
    elif opt==6:
        price=150
        d=int(input("enter the  quantity"))
        total+=price*d
        print("subtotal-",total)
        return orders()
    elif opt==7:
        price=60
        d=int(input("enter the  quantity"))
        total+=price*d
        print("subtotal-",total)
        return orders()
    elif opt==8:
        price=30
        d=int(input("enter the  quantity"))
        total+=price*d
        print("subtotal-",total)
        return orders()
    elif opt==9:
        price=80
        d=int(input("enter the  quantity"))
        total+=price*d
        print("subtotal-",brownie)
        return orders()
    elif opt==10:
        price=45
        d=int(input("enter the  quantity"))
        total+=price*d
        print("subtotal-",total)
        return orders()
    elif opt==11:
        print("enter the necessary details")
        return payment()
    
    elif opt==0:
        return customer()
    else:
        return orders()

def customer():
    global total
    global idl
    total=0
    query="insert into customer(customer_id,name,phone_no,city) values (%s,%s,%s,%s)"
    idl= input("Enter your customer ID")
    name =input("Enter your Name")
    phn=input("Enter phone.no")
    city=input("Enter your city")
    val=(idl,name,phn,city)
    mycursor.execute(query,val)
    mydb.commit()
    print("Record Inserted")
    return orders()

def login():
    print("enter your reg customer id:")
    cusid=int(input())
    if cusid==101:
        print ("valid user")
        return customer()
    elif cusid==102:
        print ("valid user")
        return customer()
    elif cusid==103:
        print("valid user")
        return customer()
    elif cusid==104:
        print ("valid user")
        return customer()
    elif cusid==105:
        print ("valid user")
        return customer()
    elif cusid==106:
        print("valid user")
        return customer()
    elif cusid==107:
        print("valid user")
        return customer()
    elif cusid==108:
        print("valid user")
        return customer()
    elif cusid==109:
        print("valid user")
        return customer()
    elif cusid==110:
        print("valid user")
        return customer()
    else :
        print("invalid user")
        return login()
login()


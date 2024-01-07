import mysql.connector
mydb=mysql.connector.coonect(host="localhost",user="root",password="pras@1234",database="Snacks")
mycursor =mydb.cursor()


def order(username):
    print("1.Apple"+'\n'+"2.Watermelon"+'\n'+"3.orange"+'\n'+"4.SoftDrink"+'\n'+"5.Lays"+'\n'+"6.Biscuits"+'\n'+"7.Bingo"+'\n'+
    "8.Kitkat"+'\n'+"9.Dairymilk"+'\n'+"10.5star")
    mydict ={1:"Apple",2:"Watermelon",3:"orange",4:"SoftDrink",5:"Lays",6:"Biscuits",7:"Bingo",8:"KitKat",9:"Dairymilk",10:"5star"}
    opt = int(input("Enter Your Option:"))
    my_need = mydict[opt]
    mycursor.execute("select amount from Snacks_list where  like %s",(my_need,))
    data = mycursor.fetchone()
    cost = int(data)
    count =int(input("How much you want :"))
    global tot_cost
    tot_cost = count*cost
    mycursor.execute("insert into myorders (item_id,username,item,count,amount)values(NULL,%s,%s,%s,%s)",(username,my_need,count,tot_cost))
    mydb.commit()
    return 1

def myorders(username):
    mycursor.execute("select * from myorders where username like %s",(username))
    mycursor.fetchall()
    return 1


def userlogin(username,password):
    mycursor.execute("select * from user_details where like %s",(username,))
    user_data = mycursor.fetchall()
    u_name=user_data[0][1]
    pas= user_data[0][4]
    if u_name == username and pas == password:
        print("1 order")
        print("2 myorders")
        choi = int(input ("Enter your Choice :"))
        if choi == 1:
            order(username)
        elif choi ==2:
            myorders(username)
        else:
            print("enter correct choice") 
    return 1
    
def usersignup():
    userrname =input("Enter Your Name :")
    email =input("Enter Your email :")
    ph_no =input("Enter Your ph_no :")
    passwordd =input("Enter Your Password :")
    mycursor.execute("insert into user_details (u_id ,u_name,email,ph_no,password) values (NULL,%s,%s,%s,%s)",(userrname,email,ph_no,passwordd,))
    mydb.commit()
    print("Rigistered!!!")
    return 1



if __name__ == "__main__":
    print("Welcome to Snacks!!!")
    print("Ocder Yours Dishes")
    dest = input("user or admin :" )
    dest.lower()
    if dest =="user":
        print("Press 1 to Login \npress 2 to Singup")
        choice = int(input("your choice :"))
        if choice ==1:
            username = input("Username :")
            password = input("password")
            userlogin(username,password)
        elif choice ==2:
            usersignup()
        else:
            print("Enter Correct Choice")
    elif dest=="admin":
        pass

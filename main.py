import sqlite3

con = sqlite3.connect('login.db')
cur = con.cursor()

cur.execute('''Create Table if not exists Login(Id Primary key, email, password, phone, address)''')
con.commit()

cur.execute('''Create Table if not exists Item(Id Primary key, item_name, item_price, shop_name, category, quantity)''')
con.commit()


def update_item():
    print("update item function")


def insert_item():
    value = 1
    while value != 0:
        print("In which shop you want to enter Select that ")
        print("========= Press 1 for Walmart ========")
        print("========= Press 2 for Dollarama ========")
        print("========= Press 3 for Shopperdrug Mart ========")
        entervalue = int(input())

        if entervalue == 1:
            shop_name = "Walmart"
            value = 0
        elif entervalue == 2:
            shop_name = "Dollarama"
            value = 0
        elif entervalue == 3:
            shop_name = "Shopperdrug Mart"
            value = 0
        else:
            print("Enter value is wrong. Enter again")
    value = 1
    while value != 0:
        print("In which Category you want to enter Select that ")
        print("========= Press 1 for vegetables & fruits ========")
        print("========= Press 2 for Dessert ========")
        print("========= Press 3 for Bakery  ========")
        print("========= Press 4 for Dairy  ========")
        print("========= Press 5 for medicine  ========")
        print("========= Press 6 for household  ========")
        print("========= Press 7 for Party Craft  ========")
        print("========= Press 8 for Kitchen utencils  ========")
        print("========= Press 9 for Snacks  ========")
        print("========= Press 10 for Meat & Chicken ========")
        entervalue = int(input())

        if entervalue == 1:
            category = "Vegetables & Fruits"
            value = 0
        elif entervalue == 2:
            category = "Dessert"
            value = 0
        elif entervalue == 3:
            category = "Bakery"
            value = 0
        elif entervalue == 4:
            category = "Dairy"
            value = 0
        elif entervalue == 5:
            category = "Medicine"
            value = 0
        elif entervalue == 6:
            category = "Household"
            value = 0
        elif entervalue == 7:
            category = "Party Craft"
            value = 0
        elif entervalue == 8:
            category = "Kitchen utencils"
            value = 0
        elif entervalue == 9:
            category = "Snacks"
            value = 0
        elif entervalue == 10:
            category = "Meat & Chicken"
            value = 0
        else:
            print("Enter value is wrong. Enter again")

    value = 1
    while value != 0:
        print("Enter item name")
        item_name = input()

        cur.execute('''Select * from Item''')
        result = cur.fetchall()
        print(result)

        cur.execute('''Select * from Item where item_name=?''', (item_name,))
        result = cur.fetchone()
        print(result)
        if result is None:
            print("Enter item price")
            item_price = float(input())
            print("Enter item Quantity")
            quantity = int(input())
            cur.execute('''Select Id from Item''')
            result = cur.fetchone()
            loginid = 0
            if result is None:
                print("if")
                loginid = 1
            else:
                cur.execute('''Select Id from Item''')
                result = cur.fetchall()
                for x in result:
                    loginid = int(x[0])
                loginid = loginid + 1
            script = "INSERT INTO Item (Id, item_name, item_price, shop_name, category, quantity )" \
                     " VALUES (?, ?, ?, ?, ?, ?);"
            cur.execute(script, (loginid, item_name, item_price, shop_name, category, quantity))
            con.commit()
            print("Do you want to insert new one or not")
            print("Press y for yes and n for no")
            entervalue = input()
            if entervalue == 'y':
                value = 0
            elif entervalue == 'n':
                value = 0
            else:
                print("enter value is wrong, Enter again")
        else:
            true = 1
            while true != 0:
                print("This item already exist")
                print("Do you want to insert new one or not")
                print("Press y for yes and n for no")
                entervalue = input()
                if entervalue == 'y':
                    true = 0
                elif entervalue == 'n':
                    true = 0
                    value = 0
                else:
                    print("enter value is wrong, Enter again")
    update_stock()


def update_stock():
    value = 1
    while value != 0:
        print("========== Press 1 if you want to insert an item =========")
        print("========== Press 2 if you want to update an item =========")
        print("========== Press 0 if you want to go back to menu ========")
        entervalue = int(input())
        if entervalue == 1:
            insert_item()
        elif entervalue == 2:
            update_item()
        elif entervalue == 0:
            mainmenu()
        else:
            print("========= enter value is wrong, Enter again ==========")


def mainmenu():
    value = 1
    while value != 0:
        print("========== Press 1 Do you want to update profile ==========")
        print("========== Press 2 Do you want to update stock ==========")

        entervalue = int(input())
        if entervalue == 1:
            update_profile()
        elif entervalue == 2:
            update_stock()
        else:
            print("Enter value is wrong, Enter again")


def update_profile():
    value = 1
    while value != 0:
        print("========== Press 1 Do you want to update password ==========")
        print("========== Press 2 Do you want to update phone number ==========")
        print("========== Press 3 Do you want to update address ==========")
        print("========== Press 0 if you want to go back to menu ========")
        entervalue = int(input())
        if entervalue == 1:
            print("Enter your old password ")
            old_password = input()
            print("Enter your new password")
            new_password = input()
            cur.execute('''Update Login set password = ? where password = ?''', (new_password, old_password))
            print("password is updated")
            cur.execute('''Select * from Login''')
            result = cur.fetchall()
            con.commit()
            for x in result:
                print(x)
            print("========== Press 1 if you want to update more ==========")
            print("========== Press 2 if you want to go back to main menu ==========")
            entervalue = int(input())
            if entervalue == 2:
                mainmenu()

        elif entervalue == 2:
            print("Enter your old phone number ")
            old_phone = input()
            print("Enter your new phone number")
            new_phone = input()
            cur.execute('''Update Login set phone = ? where phone = ?''', (new_phone, old_phone))
            print("Phone is updated")
            cur.execute('''Select * from Login''')
            con.commit()
            result = cur.fetchall()
            for x in result:
                print(x)
        elif entervalue == 3:
            print("Enter your old address ")
            old_address = input()
            print("Enter your new address")
            new_address = input()
            cur.execute('''Update Login set address = ? where address = ?''', (new_address, old_address))
            print("Address is updated")
            cur.execute('''Select * from Login''')
            con.commit()
            result = cur.fetchall()
            for x in result:
                print(x)
        elif entervalue == 0:
            mainmenu()
        else:
            print("Enter value is wrong, Enter again")


def login():
    print("Enter Email")
    email = input()
    print("Enter password")
    password = input()

    cur.execute('''select * from Login where email=? AND password=?''', (email, password))
    result = cur.fetchall()
    con.commit()

    print("result ", result)
    if result is None:
        print("this user doesn't exist")
    else:
        print("else function")
        for x in result:
            print("for loop")
            print(x)

    mainmenu()


def register():
    print("Enter Email")
    email = input()
    print("Enter password")
    password = input()
    print("Enter Phone")
    phone = input()
    print("Enter Address")
    address = input()
    cur.execute('''select Id from Login''')
    result = cur.fetchone()

    loginid = 0

    if result is None:
        loginid = 1
        print("if")
    else:
        cur.execute('''select Id from Login''')
        result1 = cur.fetchall()
        print(result1)
        for x in result1:
            loginid = int(x[0])
            print(loginid)
        loginid = loginid + 1
        print("else")

    print(loginid)
    script = "INSERT INTO Login (Id, email, password, phone, address) VALUES (?, ?, ?, ?, ?);"
    cur.execute(script, (loginid, email, password, phone, address))

    print("User is succesfully registered")

    cur.execute('''select * from Login''')
    result = cur.fetchall()
    con.commit()

    for x in result:
        print(x)


print("************************************************************")
print("========== WELCOME TO Foodcart  ==========")
print("************************************************************")
value = 1
while value != 0:
    print("========== Press 1 if you want to login ==========")
    print("========== Press 2 if you want to register ==========")
    entervalue = int(input())
    print("input value is done")
    if entervalue == 1:
        print("enter value is 1")
        login()
    elif entervalue == 2:
        register()
    else:
        print("Enter value is wrong, Enter again")
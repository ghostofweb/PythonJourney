money = 0
water = 300
milk = 200
coffee = 100

def report():
    global water, coffee, milk, money
    print("Money =", money, '$')
    print("Water = ", water, 'ML')
    print("Milk = ", milk, 'ML')
    print("Coffee = ", coffee, 'gm')
    return ask()

def checkforespresso():
    global water, coffee
    if water < 50 or coffee < 18:
        print("Sorry, not enough resources")
        return ask()
    else:
        return payment(1.5)

def checkforlatte():
    global water, coffee, milk
    if water < 200 or milk < 150 or coffee < 24:
        print("Sorry, not enough resources")
        return ask()
    else:
        return payment(2.5)

def checkforcapp():
    global water, coffee, milk
    if water < 250 or milk < 100 or coffee < 24:
        print("Sorry, not enough resources")
        return ask()
    else:
        return payment(3.0)

def coffee_maker(cost, change):
    global water, coffee, milk
    if cost == 1.5:
        water -= 50
        coffee -= 18
        print("Here is your Espresso, and here is the change of $", round(change, 2))
        return ask()
    elif cost == 2.5:
        water -= 200
        milk -= 150
        coffee -= 24
        print("Here is your latte, and here is the change of $", round(change, 2))
        return ask()
    elif cost == 3.0:
        water -= 250
        milk -= 100
        coffee -= 24
        print("Here is your Cappuccino, and here is the change of $", round(change, 2))
        return ask()

def payment(cost):
    global money
    dimes = int(input("enter the dimes ($0.25) ")) * 0.25
    nickles = int(input("enter the nickles($0.05) ")) * 0.05
    pennies = int(input("enter the pennies($0.01) ")) * 0.01
    pay = dimes + nickles + pennies
    change = pay - cost
    if cost > pay:
        print("Not enough money, choose again, money refunded though lol ")
        return ask()
    else:
        return coffee_maker(cost, change)

def ask():
    global costofesp, costofcapp, costoflatte
    choice: str = input("what would you like to have(Espresso 1.5$ /latte 2.5$ /Cappuccino 3.0$ :) ").lower()
    if choice == "report":
        report()
    elif choice == "espresso":
        return checkforespresso()
    elif choice == "latte":
        return checkforlatte()
    elif choice == "cappuccino":
        return checkforcapp()
    elif choice == "off":
        return
    else:
        print("wrong input")
        return ask()

ask()

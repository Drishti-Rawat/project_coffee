from Data import MENU
profit = 0
resource= {
    'water' : 300,
    'milk' : 200,
    'coffee' : 100,
}


def is_resouces_available(order_ingrediant):
    '''Returns True when order can be made, False if ingredients are insufficient '''
    for item in order_ingrediant:
        if order_ingrediant[item]>resource[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        return True

def  process_coins():
    """Returns the total calculated from coins inserted."""
    print("please insert coins.")
    total = int(input("How many quarters? : "))*0.25
    total+= int(input("How many dimes? : "))*0.1
    total+= int(input("How many nickles? : "))*0.05
    total+= int(input("Jow many pennies? : "))*0.01
    return total

def is_transection_successful(money_received,drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received>=drink_cost:
        change = round(money_received-drink_cost,2)
        print(f"here is ${change} in change")
        global profit
        profit+=drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False

def make_coffee(drink_name,order_ingrediant):
    """Deduct the required ingredients from the resources."""
    for item in order_ingrediant:
        resource[item]-=order_ingrediant[item]
    print(f"here is your {drink_name} ☕️. Enjoy!")




is_on = True

while is_on:
   choice = input("What world you like ? (espresso/latte/cappuccino) ")
   if  choice =="off":
       is_on=False
   elif choice =="report":
       print(f"Water: {resource['water']}ml")
       print(f"Milk : {resource['milk']}ml")
       print(f"coffee: {resource['coffee']}g")
       print(f"money: ${profit}")
   else:
       drink = MENU[choice]
       if is_resouces_available(drink["ingredients"]):
           payment = process_coins()
           if is_transection_successful(payment,drink["cost"]):
               make_coffee(choice,drink["ingredients"])



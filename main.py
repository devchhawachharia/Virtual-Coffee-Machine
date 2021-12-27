MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 30,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 40,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 50,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_ingredients(ingredients):
    for item in ingredients:
        if ingredients[item] >= resources[item]:
            print(f"Sorry not enough {item}")
            return False
    return True


def input_cash():
    cash_in = 0
    rupee_10 = input("How many Rs. 10 notes?: ")
    cash_in += int(rupee_10) * 10
    rupee_20 = input("How many Rs. 20 notes?: ")
    cash_in += int(rupee_20) * 20
    rupee_50 = input("How many Rs. 50 notes?: ")
    cash_in += int(rupee_50) * 50
    rupee_100 = input("How many Rs. 100 notes?: ")
    cash_in += int(rupee_100) * 100
    return cash_in


def transaction(coffee, cash):
    if cash < MENU[coffee]["cost"]:
        print("Not enough money, Money Refunded")
        return False
    else:
        change = cash - MENU[coffee]["cost"]
        print(f"Here is your change = Rs{change}")
        print(f"Here's your {coffee}  ☕ Enjoy!!")
        return True


def update(ingredients):
    for items in ingredients:
        resources[items] -= ingredients[items]


choice = True
money = 0

while choice:
    answer = input("What would you like? Espresso/Latte/Cappuccino: ")
    answer = answer.lower()
    if answer == "report":
        print(f"Water:{resources['water']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Milk: {resources['milk']}ml")
        print(f"Money: Rs.{money}")
        choice = True

    elif answer == "espresso":
        check = check_ingredients(MENU[answer]["ingredients"])
        if check:
            cash_input = input_cash()
            success = transaction(answer, cash_input)
            if success:
                update(MENU[answer]["ingredients"])
                money += MENU[answer]['cost']
                choice = True
            else:
                choice = True
        else:
            choice = True
    elif answer == "latte":
        check = check_ingredients(MENU[answer]["ingredients"])
        if check:
            cash_input = input_cash()
            success = transaction(answer, cash_input)
            if success:
                update(MENU[answer]["ingredients"])
                money += MENU[answer]['cost']
                choice = True
            else:
                choice = True
        else:
            choice = True
    elif answer == "cappuccino":
        check = check_ingredients(MENU[answer]["ingredients"])
        if check:
            cash_input = input_cash()
            success = transaction(answer, cash_input)
            if success:
                update(MENU[answer]["ingredients"])
                money += MENU[answer]['cost']
                choice = True
            else:
                choice = True
        else:
            choice = True
    elif answer == "off":
        choice = False
    else:
        break

exit(0)

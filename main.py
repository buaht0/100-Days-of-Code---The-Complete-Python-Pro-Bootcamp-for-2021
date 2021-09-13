MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}




finance = {
    "payment": 0,
    "change": 0

}
# TODO-5: Check coins
def check_coins(ordered):
    quarters = int(input("How many quarters?:"))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    money = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    finance['change'] = money - MENU[ordered]["cost"]
    finance['payment'] += MENU[ordered]["cost"]
    return finance


# TODO-4: Check resources sufficient?
def check_resources(ordered):
    if resources["water"] >= MENU[ordered]["ingredients"]["water"]:
        resources["water"] = resources["water"] - MENU[ordered]["ingredients"]["water"]
    else:
        return f"Sorry there is not enough water."
    if ordered == "espresso":
        resources["milk"] = resources["milk"]
    elif ordered != "espresso" and resources["milk"] >= MENU[ordered]["ingredients"]["milk"]:
        resources["milk"] = resources["milk"] - MENU[ordered]["ingredients"]["milk"]
    else:
        return f"Sorry there is not enough milk."
    if resources["coffee"] >= MENU[ordered]["ingredients"]["coffee"]:
        resources["coffee"] = resources["coffee"] - MENU[ordered]["ingredients"]["coffee"]
    else:
        return f"Sorry there is not enough coffee."
    return resources


# TODO-3: Print report.
def report(ordered):
    first_flag = True
    if first_flag == True:
        first_flag = False
        return f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney:${finance['payment']}"
    else:
        d = check_resources(ordered)
        return f"Water:{d['water']}ml\nMilk: {d['milk']}ml\nCoffee: {d['coffee']}g\nMoney:{finance['payment']}"

flag = True
while flag:
    # TODO-1: Prompt user by asking "What would you like? (espresso/latte/cappuccino):
    answer = input("What would you like? (espresso/latte/cappuccino):")

    # TODO-2: Turn off the Coffee Machine by entering "off" to the prompt.
    if answer == "off":
        exit()
    elif answer == "report":
        print(report(answer))
    else:
        order = answer
        d = check_resources(order)
        if type(d) != str:
            print("Please insert coins.")
            x = check_coins(order)
            print(f"Here is ${round(x['change'],2)}.\nHere is your latte.Enjoy!")
        else:
            print(check_resources(order))












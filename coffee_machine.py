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

should_continue = True

while should_continue:

    coffee_choice = "report"

    while coffee_choice == "report":
        coffee_choice = input("What would you like? (espresso/latte/cappuccino): ")
        if coffee_choice == "report":
            print(resources)

    if MENU[coffee_choice]["ingredients"]["water"] > resources["water"]:
        print("Sorry, not enough resources.\nYour money has been returned. ")
        should_continue = False
    elif coffee_choice != "espresso":
        if MENU[coffee_choice]["ingredients"]["milk"] > resources["milk"]:
            print("Sorry, not enough resources.\nYour money has been returned. ")
            should_continue = False
    elif MENU[coffee_choice]["ingredients"]["coffee"] > resources["coffee"]:
        print("Sorry, not enough resources.\nYour money has been returned. ")
        should_continue = False

    if should_continue:
        quarters = int(input("""Please insert coins. 
How many quarters?: """))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickels?: "))
        pennies = int(input("How many pennies?: "))

        quarters_decimal = quarters * 0.25
        dimes_decimal = dimes * 0.1
        nickels_decimal = nickels * 0.05
        pennies_decimal = pennies * 0.01

        total_money = quarters_decimal + dimes_decimal + nickels_decimal + pennies_decimal

        if coffee_choice == "espresso" and should_continue:
            resources["water"] -= 50
            resources["coffee"] -= 18
        elif coffee_choice == "latte" and should_continue:
            resources["water"] -= 200
            resources["milk"] -= 150
            resources["coffee"] -= 24
        elif coffee_choice == "cappuccino" and should_continue:
            resources["water"] -= 250
            resources["milk"] -= 100
            resources["coffee"] -= 24

        cost_of_drink = MENU[coffee_choice]["cost"]

        if total_money < cost_of_drink:
            print("Insufficient change.\nMoney Returned")

        if total_money >= cost_of_drink:
            total_money -= cost_of_drink
            print(f"Here is ${round(total_money, 2)} in change.\nHere is your {coffee_choice}. Enjoy!")

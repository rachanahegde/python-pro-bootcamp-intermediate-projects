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

profit = 0

#TODO Print report by entering "report".
def report(resources, profit):
    """ Prints out the amount of water, milk, coffee, and money in machine. """
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${profit}")

#TODO 3. Check resources sufficient when the user chooses a drink
def check_resources(resources, menu, drink):
    """Returns True if there's enough water, milk, and coffee for the drink. """
    sufficient_resources = False

    water_remaining = resources["water"] - menu[drink]["ingredients"]["water"]
    if drink == "espresso":
        milk_remaining = 0
    else:
        milk_remaining = resources["milk"] - menu[drink]["ingredients"]["milk"]
    coffee_remaining = resources["coffee"] - menu[drink]["ingredients"]["coffee"]
    
    if water_remaining >= 0 and milk_remaining >= 0 and coffee_remaining >= 0:
        sufficient_resources = True
    if water_remaining < 0:
        print("Sorry there is not enough water.")
    if milk_remaining < 0:
        print("Sorry there is not enough milk.")
    if coffee_remaining < 0:
        print("Sorry there is not enough coffee.")
    
    return sufficient_resources

#TODO 4. If there are sufficient resources to make the drink selected, then the program should prompt the user to insert coins. 
#TODO 5. Process coins and check transaction successful. 
#TODO 5a. If the user hasn't inserted enough $$, tell them and refund money. 
# TODO 5b. If the user has inserted enough money, then the cost of the drink gets added to the machine as the profit. 
# TODO 5c. If the user has inserted too much money, the machine should offer change.

def payment(menu, drink, profit, quarters, dimes, nickels, pennies):
    """Processes user's payment and returns profit."""
    drink_cost = menu[drink]["cost"]
    money = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    if money < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
    elif money >= drink_cost:
        profit += drink_cost
        change = money - drink_cost
        formatted_change = "{:.2f}".format(change)
        if change > 0:
            print(f"Here is ${formatted_change} dollars in change.")
    return profit

#TODO 6. Make Coffee.
#TODO 6a. The ingredients to make the drink should be deducted from the coffee machine resources.
#TODO 7. Tell user: "Here is your {drink}. Enjoy!"

def make_coffee(resources, menu, drink):
    """Subtracts resources used to make user's drink and returns remaining resources."""
    print(f"Here is your {drink} ☕️ Enjoy!")

    water = resources["water"]
    coffee = resources["coffee"]
    milk = resources["milk"]

    water = resources["water"] - menu[drink]["ingredients"]["water"]
    coffee = resources["coffee"] - menu[drink]["ingredients"]["coffee"]
    if drink != "espresso":
        milk = resources["milk"] - menu[drink]["ingredients"]["milk"]
    
    return water, coffee, milk

#TODO 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino)
#TODO 1a. The prompt should show every time action has completed, e.g. once the drink is dispensed. The prompt should show again to serve the next customer.
#TODO 2. Check the user’s input to decide what to do next.
#TODO Turn off the Coffee Machine by entering “off” to the prompt.     

machine_running = True
while machine_running:
    user_answer = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_answer == "espresso" or user_answer == "latte" or user_answer == "cappuccino":
        if check_resources(resources, MENU, user_answer) == True:
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickels = int(input("How many nickels?: "))
            pennies = int(input("How many pennies?: "))
            profit = payment(MENU, user_answer, profit, quarters, dimes, nickels, pennies)
            resources["water"], resources["coffee"], resources["milk"] = make_coffee(resources, MENU, user_answer)
    elif user_answer == "report":
        report(resources, profit)
    elif user_answer == "off":
        machine_running = False

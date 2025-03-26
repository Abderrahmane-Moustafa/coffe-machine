# Coffee Machine Program

# Menu with available drinks, their required ingredients, and costs
COFFEE_MENU = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18},
        "price": 1.5,
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "price": 2.5,
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "price": 3.0,
    }
}

# Initial resources available in the coffee machine
AVAILABLE_RESOURCES = {"water": 300, "milk": 200, "coffee": 100}
TOTAL_EARNINGS = 0


def check_resources(drink_ingredients):
    """Check if there are enough resources to make the requested drink."""
    for ingredient in drink_ingredients:
        if drink_ingredients[ingredient] > AVAILABLE_RESOURCES[ingredient]:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True


def process_payment():
    """Accepts coin input from the user and calculates the total amount received."""
    print("Please insert coins.")
    quarters = float(input("How many quarters?: ")) * 0.25
    dimes = float(input("How many dimes?: ")) * 0.10
    nickels = float(input("How many nickels?: ")) * 0.05
    pennies = float(input("How many pennies?: ")) * 0.01
    return quarters + dimes + nickels + pennies


def validate_transaction(amount_inserted, drink_price):
    """Checks if the inserted money is sufficient for the drink and returns the result."""
    if amount_inserted >= drink_price:
        change = round(amount_inserted - drink_price, 2)
        print(f"Here is ${change} in change.")
        global TOTAL_EARNINGS
        TOTAL_EARNINGS += drink_price
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def prepare_drink(drink_name, ingredients):
    """Deducts the used ingredients from available resources and serves the drink."""
    for ingredient in ingredients:
        AVAILABLE_RESOURCES[ingredient] -= ingredients[ingredient]
    print(f"Here is your {drink_name} ☕. Enjoy!")


# Coffee machine operation loop
machine_active = True
while machine_active:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_choice == "off":
        machine_active = False  # Turn off the machine
    elif user_choice == "report":
        print(f"Water: {AVAILABLE_RESOURCES['water']}ml")
        print(f"Milk: {AVAILABLE_RESOURCES['milk']}ml")
        print(f"Coffee: {AVAILABLE_RESOURCES['coffee']}g")
        print(f"Money: ${TOTAL_EARNINGS}")
    elif user_choice in COFFEE_MENU:
        selected_drink = COFFEE_MENU[user_choice]
        if check_resources(selected_drink["ingredients"]):
            user_payment = process_payment()
            if validate_transaction(user_payment, selected_drink['price']):
                prepare_drink(user_choice, selected_drink["ingredients"])
    else:
        print("Invalid selection. Please choose a valid drink.")

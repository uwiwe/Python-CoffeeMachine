import inventory


MENU = inventory.MENU
resources = inventory.resources


is_on = True
money = 0.00


def coins(choice_cost, user_choice, machine_money):
    print("Please insert coins.")
    quarters = float(input("How many quarters?: ")) * 0.25
    dimes = float(input("How many dimes?: ")) * 0.10
    nickles = float(input("How many nickles?: ")) * 0.05
    pennies = float(input("How many pennies?: ")) * 0.01
    total = round(quarters + dimes + nickles + pennies, 2)
    change = round(total - choice_cost, 2)
    if change > 0:
        machine_money += choice_cost
        change_response = f"Here is ${change} in change. \n"
        result = f"Here is your {user_choice}, ☕ Enjoy!"
    elif change == 0:
        machine_money += choice_cost
        change_response = ""
        result = f"Here is your {user_choice}, ☕ Enjoy!"
    else:
        change_response = ""
        result = f"Sorry, ${total} is not enough money. Money refunded."
    return change_response, result, machine_money


def are_enough_ingredients(user_choice):
    enough_ingredients = True
    missing_list = []
    for ingredient in MENU[user_choice]['ingredients']:
        if resources[ingredient] < MENU[choice]['ingredients'][ingredient]:
            enough_ingredients = False
            missing_list.append(ingredient)
        else:
            resources[ingredient] -= MENU[choice]['ingredients'][ingredient]
    return enough_ingredients, missing_list


def report():
    water = f"Water: {resources['water']}ml\n"
    milk = f"Milk: {resources['milk']}ml\n"
    coffee = f"Coffee: {resources['coffee']}g\n"
    money_in_cash = f"Money: ${money}"
    return water + milk + coffee + money_in_cash


while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(report())
    elif choice in MENU:
        f_enough_ingredients, f_missing_list = are_enough_ingredients(choice)
        if f_enough_ingredients:
            print(f"{choice} would be ${MENU[choice]['cost']}")
            f_change_response, f_result, money = coins(MENU[choice]['cost'], choice, money)
            print(f_change_response + f_result)
        else:
            missing_items_str = ", ".join(f_missing_list)
            print(f"Sorry, there is not enough {missing_items_str}")
    else:
        print(f"I'm sorry, we don't have {choice}")

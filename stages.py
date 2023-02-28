# Stage 5/6: Keep track of the supplies
def check_inventory(water, milk, coffee, cup):
    if machine["water"] < water:
        return "water"
    elif machine["milk"] < milk:
        return "milk"
    elif machine["coffee"] < coffee:
        return "coffee"
    elif machine["cup"] < cup:
        return "cup"
    return None


def make_coffee(water, milk, coffee, cup, money):
    machine["water"] -= water
    machine["milk"] -= milk
    machine["coffee"] -= coffee
    machine["cup"] -= cup
    machine["money"] += money


machine = {"water": 400, "milk": 540, "coffee": 120, "cup": 9, "money": 550}
while True:
    action = input("Write action (buy, fill, take, remaining, exit): \n")
    # For one espresso, the coffee machine needs 250 ml of water and 16 g of coffee beans. It costs $4.
    # For a latte, the coffee machine needs 350 ml of water, 75 ml of milk, and 20 g of coffee beans. It costs $7.
    # For a cappuccino, the coffee machine needs 200 ml of water, 100 ml of milk, and 12 g of coffee beans. It costs $6.
    if action == "buy":
        coffee_type = input("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
        if coffee_type == "1":
            if not check_inventory(250, 0, 16, 1):
                print("I have enough resources, making you a coffee!\n")
                make_coffee(250, 0, 16, 1, 4)
            else:
                print(f"Sorry, not enough {check_inventory(250, 0, 16, 1)}!\n")
        elif coffee_type == "2":
            if not check_inventory(350, 75, 20, 1):
                print("I have enough resources, making you a coffee!\n")
                make_coffee(350, 75, 20, 1, 7)
            else:
                print(f"Sorry, not enough {check_inventory(350, 75, 20, 1)}!\n")
        elif coffee_type == "3":
            if not check_inventory(200, 100, 12, 1):
                print("I have enough resources, making you a coffee!\n")
                make_coffee(200, 100, 12, 1, 6)
            else:
                print(f"Sorry, not enough {check_inventory(200, 100, 12, 1)}!\n")
    elif action == "fill":
        machine["water"] += int(input("\nWrite how many ml of water you want to add: \n"))
        machine["milk"] += int(input("Write how many ml of milk you want to add: \n"))
        machine["coffee"] += int(input("Write how many grams of coffee beans you want to add: \n"))
        machine["cup"] += int(input("Write how many disposable cups you want to add: \n"))
        print()
    elif action == "take":
        print(f"\nI gave you ${machine['money']}\n")
        machine["money"] = 0
    elif action == "remaining":
        print(f"""\nThe coffee machine has:
{machine["water"]} ml of water
{machine["milk"]} ml of milk
{machine["coffee"]} g of coffee beans
{machine["cup"]} disposable cups
${machine["money"]} of money\n""")
    elif action == "exit":
        break

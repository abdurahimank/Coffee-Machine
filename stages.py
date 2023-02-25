# Stage 4/6: Buy, fill, take!
print("""The coffee machine has:
400 ml of water
540 ml of milk
120 g of coffee beans
9 disposable cups
$550 of money""")
machine = {"water": 400, "milk": 540, "coffee": 120, "cup": 9, "money": 550}
action = input("Write action (buy, fill, take): \n")
# For one espresso, the coffee machine needs 250 ml of water and 16 g of coffee beans. It costs $4.
# For a latte, the coffee machine needs 350 ml of water, 75 ml of milk, and 20 g of coffee beans. It costs $7.
# For a cappuccino, the coffee machine needs 200 ml of water, 100 ml of milk, and 12 g of coffee beans. It costs $6.
if action == "buy":
    coffee_type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: \n")
    if coffee_type == "1":
        machine["water"] -= 250
        machine["milk"] -= 0
        machine["coffee"] -= 16
        machine["cup"] -= 1
        machine["money"] += 4
    elif coffee_type == "2":
        machine["water"] -= 350
        machine["milk"] -= 75
        machine["coffee"] -= 20
        machine["cup"] -= 1
        machine["money"] += 7
    elif coffee_type == "3":
        machine["water"] -= 200
        machine["milk"] -= 100
        machine["coffee"] -= 12
        machine["cup"] -= 1
        machine["money"] += 6
elif action == "fill":
    machine["water"] += int(input("Write how many ml of water you want to add: \n"))
    machine["milk"] += int(input("Write how many ml of milk you want to add: \n"))
    machine["coffee"] += int(input("Write how many grams of coffee beans you want to add: \n"))
    machine["cup"] += int(input("Write how many disposable cups you want to add: \n"))
elif action == "take":
    print(f"I gave you ${machine['money']}")
    machine["money"] = 0
print(f"""The coffee machine has:
{machine["water"]} ml of water
{machine["milk"]} ml of milk
{machine["coffee"]} g of coffee beans
{machine["cup"]} disposable cups
${machine["money"]} of money""")


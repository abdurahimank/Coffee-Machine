# Project: Coffee Machine (Python)
# Stage 3/6: Estimate the number of servings
# water = 200, milk = 50, coffee = 15
coffee_machine = {"water": int(input("Write how many ml of water the coffee machine has:\n")),
                  "milk": int(input("Write how many ml of milk the coffee machine has:\n")),
                  "coffee": int(input("Write how many grams of coffee beans the coffee machine has:\n"))}
avl_coffee = min([coffee_machine["water"] // 200, coffee_machine["milk"] // 50, coffee_machine["coffee"] // 15])
rqd_coffee = int(input("Write how many cups of coffee you will need:\n"))
if rqd_coffee == avl_coffee:
    print("Yes, I can make that amount of coffee")
elif rqd_coffee < avl_coffee:
    print(f"Yes, I can make that amount of coffee (and even {avl_coffee - rqd_coffee} more than that)")
elif rqd_coffee > avl_coffee:
    print(f"No, I can make only {avl_coffee} cups of coffee")

# Stage 6/6: Brush up your code
# For one espresso, the coffee machine needs 250 ml of water and 16 g of coffee beans. It costs $4.
# For a latte, the coffee machine needs 350 ml of water, 75 ml of milk, and 20 g of coffee beans. It costs $7.
# For a cappuccino, the coffee machine needs 200 ml of water, 100 ml of milk, and 12 g of coffee beans. It costs $6.
class CoffeeMachine:
    def __init__(self, machine):
        self.machine = machine

    def check_inventory(self, water, milk, coffee, cup):
        if self.machine["water"] < water:
            return "water"
        elif self.machine["milk"] < milk:
            return "milk"
        elif self.machine["coffee"] < coffee:
            return "coffee"
        elif self.machine["cup"] < cup:
            return "cup"
        return None

    def make_coffee(self, water, milk, coffee, cup, money):
        self.machine["water"] -= water
        self.machine["milk"] -= milk
        self.machine["coffee"] -= coffee
        self.machine["cup"] -= cup
        self.machine["money"] += money

    def start(self):
        while True:
            action = input("Write action (buy, fill, take, remaining, exit): \n")
            if action == "buy":
                coffee_type = input(
                    "\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
                if coffee_type == "1":
                    if not self.check_inventory(250, 0, 16, 1):
                        print("I have enough resources, making you a coffee!\n")
                        self.make_coffee(250, 0, 16, 1, 4)
                    else:
                        print(f"Sorry, not enough {self.check_inventory(250, 0, 16, 1)}!\n")
                elif coffee_type == "2":
                    if not self.check_inventory(350, 75, 20, 1):
                        print("I have enough resources, making you a coffee!\n")
                        self.make_coffee(350, 75, 20, 1, 7)
                    else:
                        print(f"Sorry, not enough {self.check_inventory(350, 75, 20, 1)}!\n")
                elif coffee_type == "3":
                    if not self.check_inventory(200, 100, 12, 1):
                        print("I have enough resources, making you a coffee!\n")
                        self.make_coffee(200, 100, 12, 1, 6)
                    else:
                        print(f"Sorry, not enough {self.check_inventory(200, 100, 12, 1)}!\n")
            elif action == "fill":
                self.machine["water"] += int(input("\nWrite how many ml of water you want to add: \n"))
                self.machine["milk"] += int(input("Write how many ml of milk you want to add: \n"))
                self.machine["coffee"] += int(input("Write how many grams of coffee beans you want to add: \n"))
                self.machine["cup"] += int(input("Write how many disposable cups you want to add: \n"))
                print()
            elif action == "take":
                print(f"\nI gave you ${self.machine['money']}\n")
                self.machine["money"] = 0
            elif action == "remaining":
                print(f"""\nThe coffee machine has:
        {self.machine["water"]} ml of water
        {self.machine["milk"]} ml of milk
        {self.machine["coffee"]} g of coffee beans
        {self.machine["cup"]} disposable cups
        ${self.machine["money"]} of money\n""")
            elif action == "exit":
                break


machine_1 = CoffeeMachine({"water": 400, "milk": 540, "coffee": 120, "cup": 9, "money": 550})
machine_1.start()

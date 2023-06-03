# Project: Coffee Machine (Python)
# Stage 6/6: Brush up your code
# Espresso, the coffee machine needs 250 ml of water and 16 g of coffee beans. It costs $4.
# Latte, the coffee machine needs 350 ml of water, 75 ml of milk, and 20 g of coffee beans. It costs $7.
# Cappuccino, the coffee machine needs 200 ml of water, 100 ml of milk, and 12 g of coffee beans. It costs $6.
class CoffeeMachine:
    def __init__(self):
        self.machine = {"water": 400, "milk": 540, "coffee": 120, "cup": 9, "money": 550}

    def stock_checking(self, water, milk, coffee, cup):
        stock = {"water": self.machine["water"] // water, "milk": self.machine["milk"] // milk,
                 "coffee": self.machine["coffee"] // coffee, "cup": self.machine["cup"] // cup}
        for key, item in stock.items():
            if item < 1:
                print(f"Sorry, not enough {key}!\n")
                return False
        return True

    def buy(self, water, milk, coffee, cup, money):
        print("I have enough resources, making you a coffee!\n")
        self.machine["water"] -= water
        self.machine["milk"] -= milk
        self.machine["coffee"] -= coffee
        self.machine["cup"] -= cup
        self.machine["money"] += money

    def fill(self):
        self.machine["water"] += int(input("\nWrite how many ml of water you want to add:\n"))
        self.machine["milk"] += int(input("Write how many ml of milk you want to add:\n"))
        self.machine["coffee"] += int(input("Write how many grams of coffee beans you want to add:\n"))
        self.machine["cup"] += int(input("Write how many disposable cups you want to add:\n"))
        print()

    def take(self):
        print(f"\nI gave you ${self.machine['money']}\n")
        self.machine["money"] = 0

    def display(self):
        print(f"""\nThe coffee machine has:
{self.machine["water"]} ml of water
{self.machine["milk"]} ml of milk
{self.machine["coffee"]} g of coffee beans
{self.machine["cup"]} disposable cups
${self.machine["money"]} of money\n""")

    def start(self):
        while True:
            action = input("Write action (buy, fill, take, remaining, exit): \n")
            if action == "buy":
                coffee_type = input("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, "
                                    "back - to main menu: \n")
                if coffee_type == "1":
                    if self.stock_checking(250, 1, 16, 1):
                        self.buy(250, 0, 16, 1, 4)
                elif coffee_type == "2":
                    if self.stock_checking(350, 75, 20, 1):
                        self.buy(350, 75, 20, 1, 7)
                elif coffee_type == "3":
                    if self.stock_checking(200, 100, 12, 1):
                        self.buy(200, 100, 12, 1, 6)
            elif action == "fill":
                self.fill()
            elif action == "take":
                self.take()
            elif action == "remaining":
                self.display()
            elif action == "exit":
                break


machine_1 = CoffeeMachine()
machine_1.start()

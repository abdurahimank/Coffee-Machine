# Project: Coffee Machine (Python)
# Stage 4/6: Buy, fill, take!
# water = 200, milk = 50, coffee = 15
class CoffeeMachine:
    def __init__(self):
        self.machine = {"water": 400, "milk": 540, "coffee": 120, "cup": 9, "money": 550}

    def buy(self, water, milk, coffee, cup, money):
        self.machine["water"] -= water
        self.machine["milk"] -= milk
        self.machine["coffee"] -= coffee
        self.machine["cup"] -= cup
        self.machine["money"] += money

    def fill(self):
        self.machine["water"] += int(input("Write how many ml of water you want to add:\n"))
        self.machine["milk"] += int(input("Write how many ml of milk you want to add:\n"))
        self.machine["coffee"] += int(input("Write how many grams of coffee beans you want to add:\n"))
        self.machine["cup"] += int(input("Write how many disposable cups you want to add:\n"))

    def take(self):
        print(f"I gave you ${self.machine['money']}")
        self.machine["money"] = 0

    def display(self):
        print(f"""The coffee machine has:
{self.machine["water"]} ml of water
{self.machine["milk"]} ml of milk
{self.machine["coffee"]} g of coffee beans
{self.machine["cup"]} disposable cups
${self.machine["money"]} of money""")

    def start(self):
        self.display()
        action = input("Write action (buy, fill, take): \n")
        if action == "buy":
            coffee_type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: \n")
            if coffee_type == "1":
                self.buy(250, 0, 16, 1, 4)
            elif coffee_type == "2":
                self.buy(350, 75, 20, 1, 7)
            elif coffee_type == "3":
                self.buy(200, 100, 12, 1, 6)

        elif action == "fill":
            self.fill()
        elif action == "take":
            self.take()
        self.display()


machine_1 = CoffeeMachine()
machine_1.start()

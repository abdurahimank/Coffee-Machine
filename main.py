class CoffeeMachine:
    def __init__(self, water, milk, coffee_beans, cups, money):
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.cups = cups
        self.money = money

    def remaining(self):
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.coffee_beans} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"${self.money} of money")

    def fill(self):
        self.water += int(input("Write how many ml of water you want to add:\n"))
        self.milk += int(input("Write how many ml of milk you want to add:\n"))
        self.coffee_beans += int(input("Write how many grams of coffee beans you want to add:\n"))
        self.cups += int(input("Write how many disposable coffee cups you want to add:\n"))

    def take(self):
        print(f"I gave you ${self.money}")
        self.money = 0

    def buy(self, coffee_type):
        if self.cups < 1:
            print("Sorry, not enough disposable cups!")
            return None
        if coffee_type == 1:
            if self.water < 250 or self.coffee_beans < 16:
                print("Sorry, not enough water!" if self.water < 250 else "Sorry, not enough coffee beans!")
            else:
                self.water -= 250
                self.coffee_beans -= 16
                self.cups -= 1
                self.money += 4
                print("I have enough resources, making you a coffee!")
        elif coffee_type == 2:
            if self.water < 350:
                print("Sorry, not enough water!")
            elif self.milk < 75 or self.coffee_beans < 20:
                print("Sorry, not enough milk!" if self.milk < 75 else "Sorry, not enough coffee beans!")
            else:
                self.water -= 350
                self.milk -= 75
                self.coffee_beans -= 20
                self.cups -= 1
                self.money += 7
                print("I have enough resources, making you a coffee!")
        else:
            if self.water < 200:
                print("Sorry, not enough water!")
            elif self.milk < 100 or self.coffee_beans < 12:
                print("Sorry, not enough milk!" if self.milk < 100 else "Sorry, not enough coffee beans!")
            else:
                self.water -= 200
                self.milk -= 100
                self.coffee_beans -= 12
                self.cups -= 1
                self.money += 6
                print("I have enough resources, making you a coffee!")

    def start(self):
        while True:
            action = input("Write action (buy, fill, take, remaining, exit):\n")
            if action == "remaining":
                self.remaining()
                continue
            elif action == "buy":
                coffee_type = input(
                    "What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
                if coffee_type == "back":
                    continue
                else:
                    self.buy(int(coffee_type))
            elif action == "fill":
                self.fill()
            elif action == 'take':
                self.take()
            else:
                break


machine_1 = CoffeeMachine(400, 540, 120, 9, 550)
machine_1.start()

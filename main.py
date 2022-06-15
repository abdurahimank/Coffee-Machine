class CoffeeMachine:
    def __init__(self):
        self.machine = {'water': 400, 'milk': 540, 'coffee': 120, 'cup': 9, 'money': 550}

    def display(self):
        print(f'''The coffee machine has:
{self.machine['water']} ml of water
{self.machine['milk']} ml of milk
{self.machine['coffee']} g of coffee beans
{self.machine['cup']} disposable cups
${self.machine['money']} of money\n''')

    def check_availability(self, water, milk, coffee):
        available = {'water': self.machine['water'] // water, 'milk': self.machine['milk'] // milk,
                     'coffee': self.machine['coffee'] // coffee, 'cup': self.machine['cup'] // 1}
        if min(available.values()) >= 1:
            print('I have enough resources, making you a coffee!\n')
            return True
        else:
            print(f'Sorry, not enough {[key for key, item in available.items() if item < 1][0]}!\n')
            return False

    def buy(self):
        # Espresso, the coffee machine needs 250 ml of water and 16 g of coffee beans. It costs $4.
        # Latte, the coffee machine needs 350 ml of water, 75 ml of milk, and 20 g of coffee beans. It costs $7.
        # Cappuccino, the coffee machine needs 200 ml of water, 100 ml of milk, and 12 g of coffee beans. It costs $6.
        coffee = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: \n')
        if coffee == '1':
            if self.check_availability(250, 1, 16):
                self.machine = {'water': self.machine['water'] - 250, 'milk': self.machine['milk'],
                                'coffee': self.machine['coffee'] - 16, 'cup': self.machine['cup'] - 1,
                                'money': self.machine['money'] + 4}
        elif coffee == '2':
            if self.check_availability(350, 75, 20):
                self.machine = {'water': self.machine['water'] - 350, 'milk': self.machine['milk'] - 75,
                                'coffee': self.machine['coffee'] - 20, 'cup': self.machine['cup'] - 1,
                                'money': self.machine['money'] + 7}
        elif coffee == '3':
            if self.check_availability(200, 100, 12):
                self.machine = {'water': self.machine['water'] - 200, 'milk': self.machine['milk'] - 100,
                                'coffee': self.machine['coffee'] - 12, 'cup': self.machine['cup'] - 1,
                                'money': self.machine['money'] + 6}

    def fill(self):
        self.machine['water'] += int(input('Write how many ml of water you want to add: \n'))
        self.machine['milk'] += int(input('Write how many ml of milk you want to add: \n'))
        self.machine['coffee'] += int(input('Write how many grams of coffee beans you want to add: \n'))
        self.machine['cup'] += int(input('Write how many disposable cups you want to add: \n'))
        print()

    def take(self):
        print(f'I gave you ${self.machine["money"]}\n')
        self.machine['money'] = 0

    def start(self):
        while True:
            action = input('Write action (buy, fill, take, remaining, exit): \n')
            print()
            if action == 'remaining':
                self.display()
            elif action == 'buy':
                self.buy()
            elif action == 'fill':
                self.fill()
            elif action == 'take':
                self.take()
            elif action == 'exit':
                break
            else:
                print('choose from "buy, fill, take, remaining, exit"\n')


coffee_machine_1 = CoffeeMachine()
coffee_machine_1.start()

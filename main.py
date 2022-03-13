class CoffeeMachine:
    def __init__(self):
        self.status = {'water': 400, 'milk': 540, 'coffee': 120, 'cups': 9, 'money': 550}

    def display_status(self):
        print(f'''\nThe coffee machine has:
{self.status['water']} ml of water
{self.status['milk']} ml of milk
{self.status['coffee']} g of coffee beans
{self.status['cups']} disposable cups
${self.status['money']} of money\n''')

    def check_availability(self, water, milk, coffee):
        available = {'water': self.status['water'] // water, 'milk': self.status['milk'] // milk,
                     'coffee': self.status['coffee'] // coffee, 'cup': self.status['cups'] // 1}
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
        coffee = input('\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: \n')
        if coffee == '1':
            if self.check_availability(250, 1, 16):
                self.status = {'water': self.status['water'] - 250, 'milk': self.status['milk'],
                               'coffee': self.status['coffee'] - 16, 'cups': self.status['cups'] - 1,
                               'money': self.status['money'] + 4}
        elif coffee == '2':
            if self.check_availability(350, 75, 20):
                self.status = {'water': self.status['water'] - 350, 'milk': self.status['milk'] - 75,
                               'coffee': self.status['coffee'] - 20, 'cups': self.status['cups'] - 1,
                               'money': self.status['money'] + 7}
        elif coffee == '3':
            if self.check_availability(200, 100, 12):
                self.status = {'water': self.status['water'] - 200, 'milk': self.status['milk'] - 100,
                               'coffee': self.status['coffee'] - 12, 'cups': self.status['cups'] - 1,
                               'money': self.status['money'] + 6}

    def fill(self):
        self.status = {'water': self.status['water'] + int(input('\nWrite how many ml of water you want to add: \n')),
                       'milk': self.status['milk'] + int(input('Write how many ml of milk you want to add: \n')),
                       'coffee': self.status['coffee'] + int(
                           input('Write how many grams of coffee beans you want to add: \n')),
                       'cups': self.status['cups'] + int(
                           input('Write how many disposable cups of coffee you want to add: \n')),
                       'money': self.status['money']}
        print()

    def take(self):
        print(f"\nI gave you ${self.status['money']}\n")
        self.status['money'] = 0

    def start_machine(self):
        while True:
            action = input('Write action (buy, fill, take, remaining, exit): \n')
            if action == 'remaining':
                self.display_status()
            elif action == 'buy':
                self.buy()
            elif action == 'fill':
                self.fill()
            elif action == 'take':
                self.take()
            else:
                break
            continue


coffee_machine1 = CoffeeMachine()
coffee_machine1.start_machine()

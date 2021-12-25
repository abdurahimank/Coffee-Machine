def fill_machine(machine):
    machine['water'] += int(input("Write how many ml of water you want to add:"))
    machine['milk'] += int(input("Write how many ml of milk you want to add:"))
    machine['beans'] += int(input("Write how many grams of coffee beans you want to add:"))
    machine['cups'] += int(input("Write how many disposable coffee cups you want to add:"))


def buy_coffee(machine, coffee_type):
    if machine['cups'] < 1:
        print("Sorry, not enough disposable cups!")
        return None
    if coffee_type == 1:
        if machine['water'] < 250 or machine['beans'] < 16:
            print("Sorry, not enough water!" if machine['water'] < 250 else "Sorry, not enough coffee beans!")
        else:
            machine['water'] -= 250
            machine['beans'] -= 16
            machine['cups'] -= 1
            machine['money'] += 4
            print("I have enough resources, making you a coffee!")
    elif coffee_type == 2:
        if machine['water'] < 350:
            print("Sorry, not enough water!")
        elif machine['milk'] < 75 or machine['beans'] < 20:
            print("Sorry, not enough milk!" if machine['milk'] < 75 else "Sorry, not enough coffee beans!")
        else:
            machine['water'] -= 350
            machine['milk'] -= 75
            machine['beans'] -= 20
            machine['cups'] -= 1
            machine['money'] += 7
            print("I have enough resources, making you a coffee!")
    else:
        if machine['water'] < 200:
            print("Sorry, not enough water!")
        elif machine['milk'] < 100 or machine['beans'] < 12:
            print("Sorry, not enough milk!" if machine['milk'] < 100 else "Sorry, not enough coffee beans!")
        else:
            machine['water'] -= 200
            machine['milk'] -= 100
            machine['beans'] -= 12
            machine['cups'] -= 1
            machine['money'] += 6
            print("I have enough resources, making you a coffee!")


def machine_status(machine):
    print(f"""The coffee machine has:
{machine['water']} of water
{machine['milk']} of milk
{machine['beans']} of coffee beans
{machine['cups']} of disposable cups
{machine['money']} of money""")


machine = {'water': 400, 'milk': 540, 'beans': 120, 'cups': 9, 'money': 550}
while True:
    action = input("Write action (buy, fill, take, remaining, exit):")
    if action == "remaining":
        machine_status(machine)
        continue
    elif action == "buy":
        coffee_type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        if coffee_type == "back":
            continue
        else:
            buy_coffee(machine, int(coffee_type))
    elif action == "fill":
        fill_machine(machine)
    elif action == 'take':
        print(f"I gave you ${machine['money']}")
        machine['money'] = 0
    else:
        break

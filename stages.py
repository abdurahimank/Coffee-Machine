# Stage 3/6: Estimate the number of servings
water = float(input("Write how many ml of water the coffee machine has:\n"))
milk = float(input("Write how many ml of milk the coffee machine has:\n"))
coffee = float(input("Write how many grams of coffee beans the coffee machine has:\n"))
no_coffee = int(input("Write how many cups of coffee you will need:\n"))
# 1 cup of coffee needs 200ml of water, 50ml of milk and 15g of coffee beans.
coffee_stock = min([water // 200, milk // 50, coffee // 15])
if coffee_stock == no_coffee:
    print("Yes, I can make that amount of coffee")
elif coffee_stock > no_coffee:
    print(f"Yes, I can make that amount of coffee (and even {round(coffee_stock - no_coffee)} more than that)")
else:
    print(f"No, I can make only {round(coffee_stock)} cups of coffee")

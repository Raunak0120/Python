# Shopping cart


foods = []
prices = []
total = 0

while True:
    food = input("Enter your food to buy (q to Quit): ")
    if food.lower() == "q":
        break
    else:    
         price = float(input(f"Enter the price of {food}: $"))
         foods.append(food)
         prices.append(price)

print("---- Your Cart ----")

for food in foods:
    print(food, end=" ")

print()

for price in prices:
    total += price

print (f"Your total is: ${total}")    

print("----!!Thank You!!----")
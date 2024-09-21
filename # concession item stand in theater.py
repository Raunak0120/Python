# concession item stand in theater

menu = {"popcorn": 60,
        "samosa": 25,
        "lemonade": 40,
        "soda": 30,
        "chips": 20,
        "sweetcorn": 50
}

cart = []
total = 0

print("--------------!!  MENU  !!--------------")

for key, value in menu.items():
    print(f"{key:10} : {value:.2f}")
print("---------------------------------------")

while True:
    food = input("Enter Food From Menu (q to Quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("------------------  !! You'r Cart !!  ------------------")

for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Your Total is: ${total:.2f}")


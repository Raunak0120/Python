# python weight conertor

weight = float(input("Enter your Weight: "))
unit = input("Killograms or pounds? (K or L): ")

if unit == "k":
    weight = weight * 2.205
    unit = "lbs."
    print(f"Your weight is: {round(weight, 2)} {unit}")
elif unit == "l":
    weight = weight / 2.205
    unit = "kg."
    print(f"your weight is: {round(weight, 2)} {unit}")

else:
    print(f"Invalid Unit {unit}")
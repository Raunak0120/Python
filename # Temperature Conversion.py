# Temperature Conversion 

temp = float(input("Enter Temperature: "))
unit = input("Is This Temperature is in Celsius or Farhenheit (C/F): ")

if unit == "c":
    temp = round((temp * (9/5) + 32, 2))
    print(f"Converted Temperature is: {temp}°F")
elif unit == "f":
    temp = round((temp - 32) * (5/9), 2)
    print(f"Converted Temperaure is: {temp}°C")
else:
    print(f"Invalid unit {unit}")

#interest calculator

principle = 0
rate = 0
time = 0

while principle <=0:
    principle =float(input("Enter Princkple amount: "))
    if principle <=0:
        print("Principle amount can't be zero")

while rate <=0:
    rate = float(input("Enter rate: "))
    if rate <=0:
        print("Rate can't be zero")

while time <=0:
    time = int(input("Enter time: "))
    if time <=0:
        print("Time can't be zero")

total = principle * pow(1 + (rate/100), time)
print(f"Balance after {time} years is: ${total}")
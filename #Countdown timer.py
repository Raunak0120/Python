#Countdown timer
import time
my_time = int(input("Enter time in Seconds: "))

for x in range(my_time, 0, -1):
    seconds = int(x % 60)
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(2)
print("Time's Up")
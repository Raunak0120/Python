# Credit card validator
# 1. Remove any '-' or ' '
# 2. Add all the digits of odd places from right to left
# 3. Double every second digit from right to left(If digit is two digit number add 2 digit together to form single digit)
# 4. Sum the total of step 2 and 3
# 5. If sum is divisible by 10, Then credit card is valid


sum_odd_digits = 0
sum_even_digits = 0
total = 0

# Step 1

card_number = input("Enter Credit Card Number: ")
card_number = card_number.replace("-", "") #-----> ".replce("x", "y")" method is to replace the desired spaces number etc with required thing
card_number = card_number.replace(" ", "")
card_number = card_number[::-1] # ------------> this will reverse the digit of card number as we have to add digit fro right to left
#print(card_number)

# Step 2
for x in card_number[::2]: #------> here, [::2] slice the 2nd digit means lets say there is a no. 12345678 by using these it will print 1357.
    sum_odd_digits += int(x)

    #print(sum_odd_digits)

# Step 3
for x in card_number[1::2]:
    x = int(x) * 2
    if x >= 10:
        sum_even_digits += (1 + (x%10))
    else:
        sum_even_digits += x
#print(sum_even_digits)

# Step 4
total = sum_even_digits + sum_odd_digits

# Step 5

if total % 10 == 0:
    print("Credita card is !!VALID!!")
else:
    print("Credita card is !!INVALID!!")







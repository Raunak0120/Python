#email Slicer

email = input("Enter Your Email Id: ")

index = email.index("@")

username = email[:index]
domain = email[index + 1:]
print(f"Your username is: {username}\nYour domain is: {domain}")
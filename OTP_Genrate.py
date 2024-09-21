import random, os

while True:
    x = random.randrange(1111, 9999)
    os.system("cls")
    
    print('OTP : ', x)
    
    y = int(input("Enter Your OTP: "))

    if x == y:
        os.system("cls")
        print("OTP Valid: ✅")
        break
    else:
        os.system("cls")
        print("\nPlease try again: ❌\n")
        continue

print("Welcome to Website:")

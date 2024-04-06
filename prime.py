# If a number is prime or not

number = int(input("Enter a number: ")) # 10

for i in range(2, number): # 2-9
    if (number % i == 0):
        print("Not a prime")
        break
else:
    print("Prime number")
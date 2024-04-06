# 5 attempts to enter a password

login_attempts = 5
actual_password = "Hello"

while login_attempts > 0:
    password = input("Enter password:")
    if (password != actual_password):
        print("Wrong Password")
        login_attempts -= 1
        print(f"Remaining attempts: {login_attempts}")
        if (login_attempts == 0):
            print("You ran out of attempts")
    else:
        print("Login successful")
        break


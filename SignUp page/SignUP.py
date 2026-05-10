first_name = input("please Enter your name=")
last_name = input("please Enter your last name=")
email = input("please enter your email")
password = input('please enter your password')
confirm_password = input("please enter your password")

sign_up = {
    "first_name":first_name,
    "last_name":last_name,
    "email":email,
    "password":password,
    "confirm_password":password
}

if password == confirm_password:
    print("your Account created")
    print(sign_up)
else:
    print("rewrite your password")
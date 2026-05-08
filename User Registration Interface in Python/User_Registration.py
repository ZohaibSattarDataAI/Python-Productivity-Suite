#ZohaibSattarDataAI

name = input("please enter Your Name=")
email = input("please enter your email=")
password = input("please enter your password=")
number = input("please enter you phone number")
address = input("please enter your address")

input_user= {
    "User_name": name,
    "User_email":email,
    "User_password":password,
    "User_phone number" : number,
    "User_address" : address

}

print("\nUser Information:")
print(input_user)
#ZohaibSattarDataAI

import random
import string

def password_generator(length=12):
    character = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(character)for _ in range(length))
    return password


input_len = int(input("please enter password length="))

password = password_generator(input_len)

print("password generated sucessfully",password)
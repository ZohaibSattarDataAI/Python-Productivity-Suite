#ZohaibSattarDataAI

#Guess Number Game 

import random

secret = random.randint(1,10)
while True:
    guess = int(input("please Enter Your Number="))
    if guess == secret:
       print("Guess Number Successfully")
       break
    else:
        print("try again")



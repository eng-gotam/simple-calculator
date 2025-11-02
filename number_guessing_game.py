# NUMBER GUESSING GAME
import random
guess_num = int(input("Enter the number:"))
secret_number = (random.randint(1,10))

while True:
    if guess_num == secret_number:
        print(f"{guess_num} is correct and you won!")
        break
    else:
        print("you loose!")
    guess_num = int(input("Enter the number again:"))



    


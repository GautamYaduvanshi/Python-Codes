import random

number = random.randint(1, 9)

guess = int(input("Guess a number between 1 and 9: "))

if guess < number:
    print("Too low!")
elif guess > number:
    print("Too high!")
else:
    print("Exactly right!")

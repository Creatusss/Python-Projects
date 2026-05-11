import random

number = random.randint(1,100)
attempt = 0

while True:
    guess = int(input('Enter your guess number:'))
    attempt += 1

    if guess > number:
        print("Lower. Try again.")

    elif guess < number:
        print("Higher. Try again.")

    else:
        print("Correct! Congratulations")
        print(f"You guess it in {attempt} attempt/s")
        break
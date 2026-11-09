import random

async def main():
    print("Welcome to my game!")

    name = await web_input("What is your name? ")

    number = random.randint(1, 10)

    guess = await web_input(
        "Guess a number between 1 and 10: "
    )

    if int(guess) == number:
        print("You win!")
    else:
        print(f"The number was {number}.")
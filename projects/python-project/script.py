import random

async def main():
    print(r"""

              N U M B E R   G U E S S I N G   G A M E


                         .--------.
                        /  ?  ?  /|
                       /________/ |
                       |   7    | |
                       |   ?    | /
                       |________|/


                  [ ? ]  [ 1 ]  [ 2 ]  [ 3 ]
                  [ 4 ]  [ 5 ]  [ 6 ]  [ 7 ]
                  [ 8 ]  [ 9 ]  [ 0 ]  [ ? ]


                  >>> CAN YOU CRACK THE CODE? <<<

                       TEST YOUR LUCK!
                        GOOD LUCK!

""")


print("Welcome to my game!")

name = await web_input("What is your name? ")

print(f"Hi {name}!")
number = random.randint(1, 10)

guess = await web_input(
    "Guess a number between 1 and 10: "
)

if int(guess) == number:
    print("You win!")
else:
    print(f"The number was {number}.")
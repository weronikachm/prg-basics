
import random

computer = random.randint(1,6)

you = int(input("Guess the number (1-6): "))
win = you == computer
print(f'You won: {win}')

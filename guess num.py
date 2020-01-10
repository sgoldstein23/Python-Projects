#guess number
import random

randX = random.randint()
guess = input('Please enter a number: ')

while guess != int():
    print('Sorry, please input an integer')
    guess = input('Please enter a number: ')

if guess < randX:
    print("Sorry! Your guess is too low.")
    guess = input('Please guess again: ')
if guess > randX:
    print('Sorry! Your guess is too high.')
    guess = inout('Please guess again: ')
if guess == randX:
    print("Congrats! You guess correctly.")

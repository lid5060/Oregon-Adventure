from random import random
from World1 import health, water, food

health = health - random.randint(1, 10)
water = water - random.randint(1, 10)
food = food - random.randint(1, 10)

print("Your health is", health)
print("Your water is", water)
print("Your food is", food)

if health <= 0:
    print("You have died")
    exec(open('MainMenu.py').read())
if water <= 0:
    print("You have died")
    exec(open('MainMenu.py').read())
if food <= 0:
    print("You have died")
    exec(open('MainMenu.py').read())

print("Please enter 0 to go home")
menu = int(input())
if menu == 0:
    exec(open('MainMenu.py').read())
import random
health = random.randint(10, 100)
water = random.randint(10, 100)
food = random.randint(10, 100)

print("Your health is", health)
print("Your water is", water)
print("Your food is", food)

if health <= 0:
    print("You have died due to no health")
    exec(open('MainMenu.py').read())
if water <= 0:
    print("You have died due to no water")
    exec(open('MainMenu.py').read())
if food <= 0:
    print("You have died due to no food")
    exec(open('MainMenu.py').read())

# allowing the user to go home is only for development comment out or remove when completed
print("enter 0 to go home")
menu = int(input())
if menu == 0:
    exec(open('MainMenu.py').read())
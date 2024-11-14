from Stats import first_health,first_water,first_food

#used for development only
print("Your health is", first_health)
print("Your water is", first_water)
print("Your food is", first_food)

print("Text")
print("Would you like to go left or right?")
print("Enter 1 for left 2 for right")
print("Enter 0 to go home - Development Only")
movement = int(input())
if movement == 1:
    print("Debug - left selected")
    exec(open('World2.py').read())
elif movement == 2:
    print("Debug - right selected")
    exec(open('World3.py').read())
elif movement == 0:
    exec(open('MainMenu.py').read())
else:
    print("Enter 1 or 2")

if first_health <= 0:
    print("You have died due to no health")
    exec(open('MainMenu.py').read())
if first_water <= 0:
    print("You have died due to no water")
    exec(open('MainMenu.py').read())
if first_food <= 0:
    print("You have died due to no food")
    exec(open('MainMenu.py').read())
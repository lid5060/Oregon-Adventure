from Stats import second_health,second_water,second_food

print("Your health is", second_health)
print("Your water is", second_water)
print("Your food is", second_food)

if second_health <= 0:
    print("You have died")
    exec(open('MainMenu.py').read())
if second_water <= 0:
    print("You have died")
    exec(open('MainMenu.py').read())
if second_food <= 0:
    print("You have died")
    exec(open('MainMenu.py').read())

print("Please enter 0 to go home")
menu = int(input())
if menu == 0:
    exec(open('MainMenu.py').read())
from Stats import sixth_health_stat
from Stats import sixth_water_stat
from Stats import sixth_food_stat

print("Your health is", sixth_health_stat)
print("Your water is", sixth_water_stat)
print("Your food is", sixth_food_stat)

if sixth_health_stat <= 0:
    print("You have died")
    exec(open('MainMenu.py').read())
if sixth_water_stat <= 0:
    print("You have died")
    exec(open('MainMenu.py').read())
if sixth_food_stat <= 0:
    print("You have died")
    exec(open('MainMenu.py').read())

print("Please enter 0 to go home")
menu = int(input())
if menu == 0:
    exec(open('MainMenu.py').read())
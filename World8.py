from Stats import eighth_health_stat
from Stats import eighth_water_stat
from Stats import eighth_food_stat

print("Your health is", eighth_health_stat)
print("Your water is", eighth_water_stat)
print("Your food is", eighth_food_stat)

if eighth_health_stat <= 0:
    print("You have died")
    exec(open('MainMenu.py').read())
if  eighth_water_stat <= 0:
    print("You have died")
    exec(open('MainMenu.py').read())
if eighth_food_stat <= 0:
    print("You have died")
    exec(open('MainMenu.py').read())

print("Please enter 0 to go home")
menu = int(input())
if menu == 0:
    exec(open('MainMenu.py').read())
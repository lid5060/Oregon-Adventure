from Stats import fourth_health_stat
from Stats import fourth_water_stat
from Stats import fourth_food_stat

print("Your health is", fourth_health_stat)
print("Your water is", fourth_water_stat)
print("Your food is", fourth_food_stat)

if fourth_health_stat <= 0:
    print("You have died")
    exec(open('MainMenu.py').read())
if fourth_water_stat <= 0:
    print("You have died")
    exec(open('MainMenu.py').read())
if fourth_food_stat <= 0:
    print("You have died")
    exec(open('MainMenu.py').read())

print("Please enter 0 to go home")
menu = int(input())
if menu == 0:
    exec(open('MainMenu.py').read())
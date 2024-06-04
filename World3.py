from Stats import third_health_stat
from Stats import third_water_stat
from Stats import third_food_stat

print("Your health is", third_health_stat)
print("Your water is", third_water_stat)
print("Your food is", third_food_stat)

if third_health_stat <= 0:
    print("You have died")
    exec(open('MainMenu.py').read())
if third_water_stat <= 0:
    print("You have died")
    exec(open('MainMenu.py').read())
if third_food_stat <= 0:
    print("You have died")
    exec(open('MainMenu.py').read())

print("Please enter 0 to go home")
menu = int(input())
if menu == 0:
    exec(open('MainMenu.py').read())
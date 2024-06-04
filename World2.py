from Stats import second_health_stat
from Stats import second_water_stat
from Stats import second_food_stat

print("Your health is", second_health_stat)
print("Your water is", second_water_stat)
print("Your food is", second_food_stat)

if second_health_stat <= 0:
    print("You have died")
    exec(open('MainMenu.py').read())
if second_water_stat <= 0:
    print("You have died")
    exec(open('MainMenu.py').read())
if second_food_stat <= 0:
    print("You have died")
    exec(open('MainMenu.py').read())

print("Please enter 0 to go home")
menu = int(input())
if menu == 0:
    exec(open('MainMenu.py').read())
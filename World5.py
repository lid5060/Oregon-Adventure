from Stats import fifth_health_stat
from Stats import fifth_water_stat
from Stats import fifth_food_stat

print("Your health is", fifth_health_stat)
print("Your water is", fifth_water_stat)
print("Your food is", fifth_food_stat)

if fifth_health_stat <= 0:
    print("You have died")
    exec(open('MainMenu.py').read())
if fifth_water_stat <= 0:
    print("You have died")
    exec(open('MainMenu.py').read())
if fifth_food_stat <= 0:
    print("You have died")
    exec(open('MainMenu.py').read())

print("Please enter 0 to go home")
menu = int(input())
if menu == 0:
    exec(open('MainMenu.py').read())
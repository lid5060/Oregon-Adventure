from Stats import tenth_health_stat
from Stats import tenth_water_stat
from Stats import tenth_food_stat

print("Your health is", tenth_health_stat)
print("Your water is", tenth_water_stat)
print("Your food is", tenth_food_stat)

if tenth_health_stat <= 0:
    print("You have died")
    exec(open('MainMenu.py').read())
if tenth_water_stat <= 0:
    print("You have died")
    exec(open('MainMenu.py').read())
if tenth_food_stat <= 0:
    print("You have died")
    exec(open('MainMenu.py').read())

print("Please enter 0 to go home")
menu = int(input())
if menu == 0:
    exec(open('MainMenu.py').read())
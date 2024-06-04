from Stats import seventh_health_stat
from Stats import seventh_water_stat
from Stats import seventh_food_stat

print("Your health is", seventh_health_stat)
print("Your water is", seventh_water_stat)
print("Your food is", seventh_food_stat)

if seventh_health_stat <= 0:
    print("You have died")
    exec(open('MainMenu.py').read())
if seventh_water_stat <= 0:
    print("You have died")
    exec(open('MainMenu.py').read())
if seventh_food_stat <= 0:
    print("You have died")
    exec(open('MainMenu.py').read())

print("Please enter 0 to go home")
menu = int(input())
if menu == 0:
    exec(open('MainMenu.py').read())
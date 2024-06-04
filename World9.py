from Stats import ninth_health_stat
from Stats import ninth_water_stat
from Stats import ninth_food_stat

print("Your health is", ninth_health_stat)
print("Your water is", ninth_water_stat)
print("Your food is", ninth_food_stat)

if ninth_health_stat <= 0:
    print("You have died")
    exec(open('MainMenu.py').read())
if ninth_water_stat <= 0:
    print("You have died")
    exec(open('MainMenu.py').read())
if ninth_food_stat <= 0:
    print("You have died")
    exec(open('MainMenu.py').read())

print("Please enter 0 to go home")
menu = int(input())
if menu == 0:
    exec(open('MainMenu.py').read())
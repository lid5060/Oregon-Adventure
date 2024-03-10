from Stats import start_health_stat
from Stats import start_water_stat
from Stats import start_food_stat
# Now you can use some_function without having the print statement in the if __name__ == "__main__": block being executed.
print("Your health is", start_health_stat)
print("Your water is", start_water_stat)
print("Your food is", start_food_stat)
# allowing the user to go home is only for development comment out or remove when completed
print("enter 0 to go home")
menu = int(input())
if menu == 0:
    exec(open('MainMenu.py').read())
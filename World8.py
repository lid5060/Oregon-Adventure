print("hello world")
print("Please enter 0 to go home")
menu = int(input())
if menu == 0:
    exec(open('MainMenu.py').read())
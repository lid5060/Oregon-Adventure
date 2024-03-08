import subprocess
while True:
    try:
        print("enter a number")
        menu = int(input())
        if menu == 1:
            print("Menu1")
            exec(open('Menu1.py').read())
        elif menu == 2:
            print("Menu2")
        elif menu == 0:
            break
    except Exception:
        print("Error")
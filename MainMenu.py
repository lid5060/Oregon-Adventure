while True:
    try:
        print("Development menu")
        print("enter a number between 1 - 10 to jump between worlds")
        menu = int(input())
        if menu == 1:
            print("World 1")
            exec(open('World1.py').read())
        elif menu == 2:
            print("World 2")
        elif menu ==3:
            print()
        elif menu ==4:
            print()
        elif menu == 5:
            print()
        elif menu == 6:
            print()
        elif menu == 7:
            print()
        elif menu == 8:
            print()
        elif menu == 9:
            print()
        elif menu == 10:
            print()
        elif menu == 0:
            break
    except Exception:
        print("Error")
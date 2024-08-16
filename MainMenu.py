import time
while True:
    try:
        print("Development menu remove after testing")
        print("enter a number between 1 - 10 to jump between worlds or 0 to exit")
        menu = int(input())
        if menu == 1:
            print("World 1")
            exec(open('World1.py').read())
        elif menu == 2:
            print("World 2")
            exec(open('World2.py').read())
        elif menu ==3:
            print("World 3")
            exec(open('World3.py').read())
        elif menu ==4:
            print("World 4")
            exec(open('World4.py').read())
        elif menu == 5:
            print("World 5")
            exec(open('World5.py').read())
        elif menu == 6:
            print("World 6")
            exec(open('World6.py').read())
        elif menu == 7:
            print("World 7")
            exec(open('World7.py').read())
        elif menu == 8:
            print("World 8")
            exec(open('World8.py').read())
        elif menu == 9:
            print("World 9")
            exec(open('World9.py').read())
        elif menu == 10:
            print("World 10")
            exec(open('World10.py').read())
        elif menu == 0:
            print("Exiting")
            time.sleep(5)
            break
    except Exception:
        print("Error")
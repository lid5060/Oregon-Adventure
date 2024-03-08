while True:
    try:
        menu = int(input())
        if menu == 1:
            print("Menu 1")
        elif menu == 2:
            print("Menu 2")
    except Exception:
        print("Error")
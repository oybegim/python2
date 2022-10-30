import time
password = int(input("enter password"))
login = input("enter login")
variable = 0

if password != 7777:
    while variable < 4:
        variable += 1
        time.sleep(4)
        print(variable)
elif login != "login7777":
    while variable < 6:
        variable += 1
        time.sleep(6)
        print(variable)

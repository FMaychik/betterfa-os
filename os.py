import random
import sys
import datetime
import time


def tp(massage):
    print(massage)
def t():
    sys.exit()
print("Dilacs (c)")
print ("Loading BetterFa OS...")
print("For help write help")

#commands list
while True:
    c1 = input("C:\Shell: ")
    #commands
    if c1 == "help":
        print ("For help = help")
        tp("Calculator = calc")
        tp("Information = info")
        time.sleep(1)
        tp("UTC time = clock")
        tp("Shutdown = turn_off")

    elif c1 == "info":
        tp("BetterFa DOS")
        tp("BetterFa OS v 0.7")
        tp("Dilacs Studio Place 2022 - 2023 (c)")

    elif c1 == "calc":
        n1 = int(input("Type first number: "))
        do = input("Type *, /, +, - :")
        n2 = int(input("Type second number: "))
        if do == "+":
            time.sleep(0.9)
            tp(n1 + n2)
        if do == "-":
            time.sleep(0.9)
            tp(n1 - n2)
        if do == "/":
            time.sleep(0.9)
            tp(n1 / n2)
        if do == "*":
            time.sleep(0.9)
            tp(n1 * n2)


    elif c1 == "clock":
        time.sleep(1)
        dt_now = datetime.datetime.utcnow()
        print(dt_now)


    elif c1 == "turn_off":
        tp("Goodbye!")
        time.sleep(2)
        t()

    else:
        tp("Wrong command! Try again!")

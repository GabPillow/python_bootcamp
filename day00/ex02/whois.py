import sys

if  len(sys.argv) >= 3 or \
    (sys.argv[1][0] != '-' and not sys.argv[1].isdigit() or \
    (sys.argv[1][0] == '-') and not sys.argv[1][1:].isdigit()):
    print("ERROR")
else:
    number = int(sys.argv[1])
    if number == 0:
        print("I'm zero")
    elif number % 2 == 0:
        print("I'm even")
    else:
        print("I'm odd")

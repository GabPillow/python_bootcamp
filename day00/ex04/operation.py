import sys

if len(sys.argv) < 3:
    sys.exit("InputError : Not enough arguments")
if len(sys.argv) > 3:
    sys.exit("InputError : Too many arguments")
for nbr in sys.argv[1:]:
    if  (nbr[0] != '-' and not nbr.isdigit()) \
        or (nbr[0] == '-' and not nbr[1:].isdigit()):
        sys.exit("InputError : Only numbers")

nbr1 = int(sys.argv[1])
nbr2 = int(sys.argv[2])
print("Sum:        ", nbr1 + nbr2, "\n"\
"Difference: ", nbr1 - nbr2, "\n"\
"Product:    ", nbr1 * nbr2, "\n"\
"Quotient:   ", (nbr1 / nbr2) if nbr2 != 0 else "ERROR div by zero", "\n"\
"Remainder:  ", (nbr1 % nbr2) if nbr2 != 0 else "ERROR modulo by zero", "\n")
        

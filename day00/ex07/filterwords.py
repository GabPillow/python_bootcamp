import sys

def list_maker(str=''):
    for c in str:
        if not c.isdigit() and not c.isalpha():
           str = str.replace(c, ' ')
    return (str.split(' '))

if  len(sys.argv) > 3 or len(sys.argv) < 3 or not sys.argv[2].isdigit():
    sys.exit("ERROR")

str = sys.argv[1]
lst = list_maker(str)
lenlim = int(sys.argv[2]) 
for element in lst:
    if len(element) <= lenlim:
        lst.remove(element)

print(lst)

import sys
import string

def list_maker(s=''):
    for c in string.punctuation:
        s = s.replace(c, ' ')
    return (s.split())

if  len(sys.argv) > 3 or len(sys.argv) < 3 or not sys.argv[2].isdigit():
    sys.exit("ERROR")

str = sys.argv[1]
lst = list_maker(str)
lenlim = int(sys.argv[2]) 
for element in lst:
    if len(element) <= lenlim:
        lst.remove(element)

print(lst)

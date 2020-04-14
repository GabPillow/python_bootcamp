import sys

morse_code = {'A':'.-', 'B':'-...', \
                'C':'-.-.', 'D':'-..', 'E':'.', \
                'F':'..-.', 'G':'--.', 'H':'....', \
                'I':'..', 'J':'.---', 'K':'-.-', \
                'L':'.-..', 'M':'--', 'N':'-.', \
                'O':'---', 'P':'.--.', 'Q':'--.-', \
                'R':'.-.', 'S':'...', 'T':'-', \
                'U':'..-', 'V':'...-', 'W':'.--', \
                'X':'-..-', 'Y':'-.--', 'Z':'--..', \
                '1':'.----', '2':'..---', '3':'...--', \
                '4':'....-', '5':'.....', '6':'-....', \
                '7':'--...', '8':'---..', '9':'----.', \
                '0':'-----' }

if len(sys.argv) > 2 or len(sys.argv) < 2 or not \
sys.argv[1].isalnum():
    sys.exit("ERROR")

morse_string = '-.-.-'
if sys.argv[1] != '':
    morse_letter = sys.argv[1].upper()
for c in morse_letter:
    morse_string = morse_string + morse_code[c]
morse_string = morse_string + '...-.-'
print(morse_string)
    
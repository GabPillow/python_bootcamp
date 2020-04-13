import sys

final_string = ""

for arg in reversed(sys.argv[1:]):
    if arg != sys.argv[-1]:
        final_string = final_string + " "
    final_string = final_string + arg [::-1]
print(final_string.swapcase()) 
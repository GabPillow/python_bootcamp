import random

print('Hey! Guess my number!\nType exit to quit!')
number = random.randint(1, 99)

try_out = 0
answer = '0'
while int(answer) != number:
    try_out += 1
    answer = input('Between 1 and 99?')
    if (answer[0] != '-' and not answer.isdigit() \
    or (answer[0] == '-') and not answer[1:].isdigit()):
        if answer == 'exit':
            print('ok bye!')
            exit()
        print('NOT A NUMBER')
    else:
        if int(answer) > number:
            print('Too high')
        if int(answer) < number:
            print('too low')
if number == 42:
    print('You\'ve been faster than a computer in a certain story...')
if try_out == 1:
    print('In one try? You\'re a lucky one')
else:
    print('You did it! In {} try'.format(try_out))

    


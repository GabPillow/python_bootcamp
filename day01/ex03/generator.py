import datetime

def random(min= 0, max = 100):
    x = datetime.datetime.now()
    x = x.microsecond
    while x < min:
        x = x * 10
    max = max + 1
    while x > max:
        x = x % max + 0.5
    return int(x)

def generator(text, sep=" ", option=None):

    if not isinstance(text, str) or len(sep) != 1:
        quit('ERROR')

    ret_lst = text.split(sep)
    t_ret_lst = []
    if option == 'shuffle':
        while ret_lst:
            rd = random(0, len(ret_lst) - 1)
            t_ret_lst.append(ret_lst[rd])
            ret_lst.pop(rd)
    elif option == 'ordered':
        ret_lst.sort(key=str.lower)
        t_ret_lst = ret_lst
    elif option == 'unique':
        for w in ret_lst:
            if w not in t_ret_lst:
                t_ret_lst.append(w)
    else:    
        t_ret_lst = ret_lst
    for w in t_ret_lst:
        yield w
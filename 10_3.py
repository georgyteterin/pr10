fib_dic = {1: 1, 2: 1}  

def fib_mem(n):
    znach = fib_dic.get(n)
    if znach is None:
        znach = fib_mem(n-2) + fib_mem(n-1)
        fib_dic[n] = znach
    return znach
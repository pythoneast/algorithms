# Uses python3

from random import randint

'''
This is the naive algorithm for the fibonacci problem
'''
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

#n = int(input())
#print(calc_fib(n))

def faster_fib(n):
    #create an array
    arr = list(range(0,n))
    arr[0] = 0
    arr[1] = 1

    for index from 2 to n:
        f[i] <- f[i -1] + f[i-2]
    ret f[n]
    pass
def fib_stressTest():
    rand_num = randint(0,46)
    print('Number used in test is ', rand_num)
    result = calc_fib(rand_num)
    return result


if __name__ == "__main__":
    print(fib_stressTest())



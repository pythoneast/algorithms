# Uses python3

from random import randint

'''
This is the naive algorithm for the fibonacci problem
'''
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)




def faster_fib(n):
    arr = [0,1]
    if n == 0:
        return 0

    for i in range(2,n+1):
        t = arr[i-1] + arr[i-2]
        arr.append(t)

    return arr[-1]

def fib_last_digit(n):
    arr = [0,1]
    if n == 0:
        return 0
    for i in range(2,n+1):
        t = (arr[i-1] + arr[i-2])%10
        arr.append(t)
    return arr[-1]
    
 
def fib_stressTest():
    while True:
        rand_num = randint(0,46)
        print('Number used in test is ', rand_num)
        res1 = calc_fib(rand_num)
        res2 = faster_fib(rand_num)
        if res1 != res2:
            print('Wrong Answer',res1,res2)
            break
        else:
            print('################OK####################')


if __name__ == "__main__":
    number = int(input())
    #print(faster_fib(number))
    print(fib_last_digit(number))
    #fib_stressTest()



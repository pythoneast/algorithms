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
'''
0 + 1 = 1
1 + 1 = 2
1 + 2 = 3
2 + 3 = 5
3 + 5 = 8

'''

def faster_fib(n):
    arr = [0,1]
    arr1=[]

    for i in range(2,n):
        t = arr[i-1] + arr[i-2]
        arr.append(t)
        print(t)
    '''
   
    f1 = 0
    f2 = 1
    if n == 0:
        return f1
    if n == 1:
        return f2
    current_sum = 1    
    for i in range(2,n):
        current_sum = current_sum + f2
        #print(current_sum)
        f1 = f2
        f2 = current_sum

    return current_sum
  '''
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
    print(faster_fib(number))
    #fib_stressTest()



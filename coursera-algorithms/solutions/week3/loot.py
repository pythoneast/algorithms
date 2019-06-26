#python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0
    # write your code here
    #1 10 
    #500 30

        
    z = weights/values
    if values > capacity:
        z *= capacity

    return z


if __name__ == "__main__":
    print(get_optimal_value(10,500,30))
    #print(500/30)
    '''
    n, capacity = list(map(int,input().split(' ')))
    print(n)
    while n > 0:

        #get_optimal_value(n,5,20)
        n -=1
        print(n)
    '''

    '''
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
    '''
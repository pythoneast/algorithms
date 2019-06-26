#python3
import sys

def get_optimal_value(capacity,values, weights):


    val_item = []
    max_index = 0
    value_knap = 0

    #calculate the value of each item
    for i in range(len(weights)):
        value = values[i]/weights[i]
        val_item.append(value)

    #determine which value is bigger
        if value > max_index:
            max_index = i
    print(max_index, "max index")

    #figure out how much weight of the most value items you can use
    if capacity > 0:
        value_knap += values[max_index]
        capacity -= weights[max_index]
    else:
        #remove from greatest value from array index and use the second largest value
        values.pop(max_index)
        weights.pop(max_index)
    
    print(value_knap)


    # write your code here
    #1 10 
    #500 30
    return val_item

'''
    z = weights/values
    if values > capacity:
        z *= capacity
'''


if __name__ == "__main__":
    print(get_optimal_value(50,[60,100,120],[20,50,30]))
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
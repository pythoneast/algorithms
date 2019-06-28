#python3
import sys

def get_optimal_value(capacity,values, weights):

    #values for each item v/w by index
    val_item = []

    #the position of the item with the most value
    max_index = 0

    #the total value of the knapsack
    value_knap = 0

    #while the bag is not full - when capacity is greater 0 
    while capacity >0:
        #calculate the value of each item
        for i in range(len(weights)):
            value = values[i]/weights[i]
            val_item.append([value,weights[i]])

        #determine which value is bigger
            if value > max_index:
                max_index = i
        

        #if the weight of the item cost more than capcity of the knapsack
        if val_item[max_index][1] > capacity:
            value_knap += val_item[max_index][0] * capacity
            capacity -= val_item[max_index][1]
            #print(value_knap)

        else:
            value_knap += val_item[max_index][0] * val_item[max_index][1]
            capacity -= val_item[max_index][1]
            val_item.pop(max_index)

        #print("value of knapsack",value_knap)
        #print("how much capcity left", capacity)
        #print(val_item)

    return value_knap



if __name__ == "__main__":
    n, cap = list(map(int,input().split(' ')))
    v = []
    w = []
    '''
    3 50
     60 20 
     100 50 
     120 30
    '''
    while n > 0:

        #get_optimal_value(n,5,20)
        max_input = list(map(int,input().split(' ')))
        v.append(max_input[0])
        w.append(max_input[1])

        n -=1
        #print(v)
        #print(n)
    print(get_optimal_value(cap,v,w))

    #print(get_optimal_value(50,[60,100,120],[20,50,30]))
    #print(get_optimal_value(10,[500],[30]))
    #print(500/30)
    '''
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
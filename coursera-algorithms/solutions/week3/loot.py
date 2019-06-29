#python3

import sys

def get_optimal_value(capacity,values, weights):

    #values for each item v/w by index
    val_item = []
    
    #greatest value
    max_value = 0

    #the position of the item with the most value
    max_index = 0

    #the total value of the knapsack
    value_knap = 0

    #while the bag is not full - when capacity is greater 0 
        #calculate the value of each item
    for i in range(len(weights)):
        ratio = values[i]/weights[i]
        val_item.append([ratio,weights[i]])
        
        #determine which value is bigger
        if ratio > max_value:
            max_value = ratio
            max_index = i
        
    print(max_value,max_index)
    print(val_item)
    
    #if capacity < weight
    #then take the ratio
    #update the capcity

    if capacity < val_item[max_index][1]:
        capacity = capacity/val_item[max_index][1]
        print(c_val)
        
        
    #else if capcity >= weight 
    #take the entire weight
    #update the capcity

    elif capacity >= val_item[max_index][1]:
        capacity = capacity - val_item[max_index][1]
        print(capacity)
        
        
    #update the list of items
    val_item.pop(max_index)
    
    #find the max_index and do the if statement again

    
    
    
    #capacity - weight
    #update the list of items
    
        #print("value of knapsack",value_knap)
        #print("how much capcity left", capacity)
        #print(val_item)

    return value_knap
    
'''
1 1000
500 30



'''



if __name__ == "__main__":

    print(get_optimal_value(50,[60,100,120],[20,50,30]))
    #print(get_optimal_value(10,[500],[30]))
    #print(500/30)
   


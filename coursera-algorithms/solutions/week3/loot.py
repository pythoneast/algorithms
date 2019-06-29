
'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.
'''
#https://codereview.stackexchange.com/questions/150677/knapsack-greedy-algorithm-in-python
import sys 
def get_optimal_value (capacity, values, weights):
    n = len (weights)
    
    #values for each item v/w by index
    val_item =[]

    #greatest value
    max_value = 0
    #the position of the item with the most value
    max_index = 0
    
    #the total value of the knapsack
    value_knap = 0
    #while the bag is not full - when capacity is greater 0
    #calculate the value of each item
    #find the value of each weight
    for i in range (len (weights)):
        ratio = values[i] / weights[i] 
        val_item.append([ratio, weights[i]])
        
    #sort from largest to smallest    
    val_item.sort(reverse = True)
    #print(val_item)
    
    #while there are items available go through the list of loot items >:)
    while len(val_item) > 0:
        
        #if the weight is more than the capacity of the loot bag
        #return a fraction of the value of the item
        
        if capacity<val_item[0][1]:
            capacity = capacity / val_item[0][1]
            #print(val_item)
            value_knap = capacity * values[0] 
            val_item.pop(0) 
            
        #if the the bag can hold the the entire weight of the largest value item "just put it the bag...."   
        elif capacity >= val_item[0][1]:
            #update the weight of the bag
            capacity = capacity - val_item[0][1]
            
            #value * weight
            #print(val_item[0][0]*val_item[0][1])
            value_knap = value_knap + (val_item[0][0]*val_item[0][1])
            print(value_knap)
            val_item.pop(0)
    print(value_knap)
    
            
            

    return value_knap 
    


  

if __name__== "__main__":
    print (get_optimal_value (50,[60, 100, 120],[20, 50, 30]))
    #print(get_optimal_value(1000,[500],[30]))
    #print(get_optimal_value(10,[500],[30]))
    #print(500/30)

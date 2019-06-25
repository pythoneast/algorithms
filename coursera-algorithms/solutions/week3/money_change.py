#python3
import sys

'''
    Naive Algorithim 
'''
def get_change(m):
    #write your code here
    all_change = []
    change_counter = {"ten":0,"five":0,"one":0}
    while m  > 0:
        if m -10 > 0:
            print(10)
            m  = m - 10
            change_counter["ten"] +=1
        
        if m - 5 >= 0:
            print(5)
            m = m - 5
            change_counter["five"]+=1
        
        if m - 1 >= 0:
            print(1)
            m = m - 1
            change_counter["one"]+=1


    

    return change_counter

if __name__ == '__main__':
    print(get_change(28))



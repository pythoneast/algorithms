#python3
import sys

'''
    Naive Algorithim 
'''
def get_change(m):
    #write your code here
    total_counter = 0
    change_counter = {"ten":0,"five":0,"one":0}
    choices = [10,5,1] 
    while m - choices[0] >=0:
        print(10)
        m = m -10
    while m - choices[1] >= 0:
        print(5)
        m = m -5
    while m - choices[2] >= 0:
        print(1)
        m = m -1
    
    '''
    for i in choices:
        if m - i >=0: 
            m = m - i
            print(i)
            print(m,"###sum##")
    '''
    
    '''
    while m  > 0:
        if m -10 > 0:
            print(10)
            m  = m - 10
            change_counter["ten"] +=1
            total_counter +=1
        
        if m - 5 >= 0:
            print(5)
            m = m - 5
            change_counter["five"]+=1
            total_counter +=1
        
        if m - 1 >= 0:
            print(1)
            m = m - 1
            change_counter["one"]+=1
            total_counter +=1


    '''

    return None

if __name__ == '__main__':
    number = int(input())
    print(get_change(number))



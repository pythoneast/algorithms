#python3
import sys

'''
    Naive Algorithim 
'''

#BigO n^3
def get_change(m):
    #write your code here
    total_counter = 0
    choices = [10,5,1] 

    while m - choices[0] >=0:
        #print(10)
        m = m -10
        total_counter +=1

    while m - choices[1] >= 0:
        #print(5)
        m = m -5
        total_counter +=1
    while m - choices[2] >= 0:
        #print(1)
        m = m -1
        total_counter +=1

    return total_counter

#Big O n^2
def get_change_fast(m):
    total_counter = 0
    choices = [10,5,1] 

    for i in range(3):
        while m - choices[i]>=0:
            #print(choices[i])
            m -=choices[i]
            total_counter += 1
            
    return total_counter

if __name__ == '__main__':
    number = int(input())
    print(get_change_fast(number))



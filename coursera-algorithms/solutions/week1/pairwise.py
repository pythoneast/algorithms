#python 3

'''
Resources: https://stackoverflow.com/questions/126524/iterate-a-list-with-indexes-in-python
'''

import random

'''
Original pairwise product algorithm
Slowest run time
'''

def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product

'''
    Faster pairwise product algorithm
    faster runtime
'''
def pairwise1(numbers):
    max_index1 = 0
    max_index2 = 0
    
    #find the highest number
    for i, val in enumerate(numbers):
        if numbers[i] > numbers[max_index1]:
            max_index1 = i

    #find the second highest number
    for j, val in enumerate(numbers):
        if j != max_index1 and numbers[j] > numbers[max_index2]:
            max_index2 = j
    
    #print(max_index1)    
    #print(max_index2)

    return int(numbers[max_index1]) * int(numbers[max_index2])    
  


'''
    Another solution to the pairwise product 
    Even faster run time (probably)
'''
def pairwise(arr):
    arr.sort(reverse = True)
    solution = int(arr[0]) * int(arr[1])
    return solution


def stressTess(n,m):
    arr = []
    while true:
        for x in range(5):
            arr.append(x)

'''

StressTest(N,M): 
while true: n←random integer between 2 and N allocate array A[1...n] 
    for i from 1 to n: A[i]←random integer between 0 and M print(A[1...n])
         result1←MaxPairwiseProductNaive(A) 
        result2←MaxPairwiseProductFast(A) 
if result1 =result2: print(“OK”) else: print(“Wrong answer: ”, result1, result2) return


'''



if __name__ == '__main__':
    length = input()
    numbers = input().split(' ')
    #answer = pairwise(numbers)
    answer = pairwise1(numbers)
    print(answer)

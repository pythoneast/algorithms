#python 3

'''
Resources: https://stackoverflow.com/questions/126524/iterate-a-list-with-indexes-in-python
'''

from random import randint
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


 

def stressTest():
    arr = []
    while True:
        for x in range(5):
            random_num = random.randint(2,101)
            arr.append(random_num)

        result1 = max_pairwise_product(arr)
        result2 = pairwise1(arr)

        if result1 != result2:
            print("wrong answer: {} **** {}".format(result1, result2))
        else:
            print("############################################# \n Ok")

        return


        




if __name__ == '__main__':
    '''
    length = input()
    numbers = input().split(' ')
    #answer = pairwise(numbers)
    answer = pairwise1(numbers)
    print(answer)
    '''

    while True:
        arr = []
        for x in range(5):
            random_num = randint(2,101)
            arr.append(random_num)
        print(arr)
        print('####')
        result1 = max_pairwise_product(arr)
        result2 = pairwise1(arr)
        print("Result 1 {}, Result2 {}".format(result1,result2))
        #print(result1)
        #print(result2)

        if result1 != result2:
            print("wrong answer: {} **** {}".format(result1, result2))
            break
        else:
            print("############################################# \n Ok", result1, result2)

    

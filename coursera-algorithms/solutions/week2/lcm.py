#python 3
from gcd import gcd_fast


def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

def lcm(a,b):
    #Step 1 Find the GCF for two numbers
    gcd = gcd_fast(a,b)

    #Step 2 divide the gcf into either number
    x = a//gcd

    #Step 3 Take that answer  multiply it by the other number.
    y = x*b

    return y

def stress_test():
    while True:

        pass
    

if __name__ == "__main__":
    numbers = input().split(' ')
    num1 = int(numbers[0])
    num2 = int(numbers[1])
    print(lcm(num1,num2))
    '''
    print(lcm(18,30))
    print(lcm(6,8))
    print(lcm(761457, 614573))
    '''

'''
Step 1)  Find the GCF for the two numbers.

For 18 and 30, GCF is 6.

Step 2)  Divide that GCF into either number; it doesn’t matter which one you choose, so choose the one that’s easier to divide.

Choose 18. Divide 18 by 6. Answer = 3.

Step 3)  Take that answer and multiply it by the other number.

3 x 30  =  90

Step 4)  Celebrate …

… because the answer you just got is the LCM. It’s that easy.

Note:  if you want to check that this technique does work, divide by the other number, and see if you don’t get the same answer.
'''
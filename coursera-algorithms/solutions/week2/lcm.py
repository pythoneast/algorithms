#python 3
#from gcd import gcd_fast


def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

def gcd_fast(a,b):
    factors = []
    if a == b :
        return a
    if a == 1:
        return 1

    while a != 0:
        remainder = b % a
        b = a
        a = remainder
        #print(a)
        factors.append(a)
        #print(factors)
        
    return factors[-2]



def lcm(a,b):
    if a == 0 or b == 0:
        return 0
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


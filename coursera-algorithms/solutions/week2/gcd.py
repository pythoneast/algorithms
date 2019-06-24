#python3
import sys

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

'''
a prime is the remainder when a/b
#eculidean algorithm for gcd visit youtube
'''
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
    

if __name__ == "__main__":
    #print(gcd_fast(18,35))
    #print(gcd_fast(28851538 ,1183019 ))
    numbers = input().split(' ')
    #print(numbers)
    x = int(numbers[0])
    y = int(numbers[1])
    #print(x,y)
    print(gcd_fast(x,y))


    
    
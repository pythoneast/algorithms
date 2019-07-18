# Uses python3
import sys

def majority(a, arr):
    if len(arr) == 0:
        return None

    if len(arr) == 1:
        return a[0]

    half = len(arr) // 2
    left = arr[0:half]
    right = arr[half:]

    if left == right:
        return left

    if arr.count(left) > half:
        return left
    
    if arr.count(right) > half:
        return right

    
    

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)

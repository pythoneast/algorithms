#python 3
import sys
def get_optimal_value(capacity, weights, values):
    value = 0.

    valuePerWeight = sorted([[v / w, w] for v,w in zip(values,weights)], reverse=True)
    print(valuePerWeight)
    while capacity > 0 and valuePerWeight:
        maxi = 0
        idx = None
        for i,item in enumerate(valuePerWeight):
            if item [1] > 0 and maxi < item [0]:
                maxi = item [0]
                idx = i

        if idx is None:
            return 0.

        v = valuePerWeight[idx][0]
        w = valuePerWeight[idx][1]

        if w <= capacity:
            value += v*w
            capacity -= w
        else:
            if w > 0:
                value += capacity * v
                return value
        valuePerWeight.pop(idx)

    return value

if __name__ == "__main__":
    '''
    n, cap = list(map(int,input().split(' ')))
    v = []
    w = []
    while n > 0:
        #get_optimal_value(n,5,20)
        max_input = list(map(int,input().split(' ')))
        v.append(max_input[0])
        w.append(max_input[1])

        n -=1
    '''
    n = 3
    cap = 50
    v = [60, 100, 120]
    w = [20, 50, 30]
    opt_value = get_optimal_value(cap, w, v)
    print("{:.10f}".format(opt_value)) # print 180.0000000000
# python3
import sys





#python3
def compute_min_refills(distance, tank, stops):
    # write your code heregi
    n = len(stops)
    first_stop = 0
    max_index = 0


  


    for i in range(n):
        #find the maximum first stop
        if tank - stops[i] > 0:
            max_index = i
        #can i reach my next gas station
        while tank  - stops[i ] > 0:
            print('hello')
            #can I reach my next destination?


        print(stops[max_index])
    


    

if __name__ == '__main__':
    print(compute_min_refills(950,400,[200,375,550,750]))
    #print(compute_min_refills(10,3,[1,2,5,9]))
    #d, m, _, *stops = map(int, sys.stdin.read().split())
    #print(compute_min_refills(d, m, stops))
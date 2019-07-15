#python 3
import sys



def compute_min_refills(distance ,max_run, gas_stations):
    stops = 0
    last_stop_value = 0
    index = 0
    gas_stations.append(distance)
    while index < len(gas_stations):
        if gas_stations[index] - last_stop_value <= max_run:
            index += 1
            continue
        elif gas_stations[index] - gas_stations[index-1] > max_run or index == 0:
            return -1
        else:
            last_stop_value = gas_stations[index-1]
            stops += 1
    return stops
    


   
 

if __name__ == '__main__':
    #print(compute_min_refills(950,400,[200,375,550,750]))
    #print(compute_min_refills(500,200,[100,200,300,400]))

    #print(compute_min_refills(10,3,[1,2,5,9]))
    d = int(input())
    m = int(input())
    _ = int(input())
    stops = list(map(int,input().split()))
    print(compute_min_refills(d, m, stops))


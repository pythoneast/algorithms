# python3
import sys





def compute_min_refills(distance, tank, stops):
    # write your code heregi
    stops.sort(reverse=True)
    num_stops = 0
    first_stop = 0
    max_index = 0
    #whats the further stop you can go?
    for i, stop in enumerate(stops):
        if tank - stop > 0:
            first_stop = stop
            max_index = i
            num_stops +=1
            break
    print(first_stop)
    
    stops = stops[:max_index]
    for i, stop in enumerate(stops):
        if stops[i] - first_stop < tank:
            num_stops +=1
            first_stop = stop
            break
        else:
            print("too far away")
    print(stops)
    print(first_stop)
    if distance - first_stop < tank:
        print(num_stops)
    
        
    return -1

if __name__ == '__main__':
    #print(compute_min_refills(950,400,[200,375,550,750]))
    print(compute_min_refills(10,3,[1,2,5,9]))
    #d, m, _, *stops = map(int, sys.stdin.read().split())
    #print(compute_min_refills(d, m, stops))
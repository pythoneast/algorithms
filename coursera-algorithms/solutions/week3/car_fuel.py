#python 3


def compute_min_refills(distance, tank, stops):

    num_stops = 0
    n = len(stops)
    while n > 0:
        smallest = tank - stops[0]

        for i,v in enumerate(stops):
            
            miles = tank - stops[i]
        
            if miles > 0 and smallest > miles:
                smallest = miles
                d_travel = stops[i] + tank
                num_stops += 1
        
        stops = stops[i-1:]
        smallest = d_travel - stops[0]
        for i,v in enumerate(stops):
            #print(d_travel - stops[i])
            if d_travel - stops[i] < 0:
                return -1
                break
            
            elif d_travel - stops[i] < tank and smallest > d_travel - stops[i]:
                #print(stops[i])
                num_stops += 1
            
        #print(stops)
        stops = stops[i:]
        #print(stops)
        if len(stops) == 1:
            #print(num_stops)
            return num_stops
            break

  
        n -= 1
   
if __name__ == '__main__':
    print(compute_min_refills(950,400,[200,375,550,750]))
    print(compute_min_refills(10,3,[1,2,5,9]))
    #d, m, _, *stops = map(int, sys.stdin.read().split())
    #print(compute_min_refills(d, m, stops))


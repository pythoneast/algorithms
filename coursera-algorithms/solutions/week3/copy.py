#python3
 
tank = 3
n = 4 
distance = [1, 2 ,5, 9]
'''
distance = [200,375,550,750]
tank = 400
stops = 0
d_travel = 0
n =4
'''
stops = 0

while n > 0:
    
    smallest = tank - distance[0]

    for i,v in enumerate(distance):
        
        miles = tank - distance[i]
    
        if miles > 0 and smallest > miles:
            smallest = miles
            d_travel = distance[i] + tank
            stops += 1
            print(smallest)
        
    distance = distance[i-1:]
    smallest = d_travel - distance[0]
    for i,v in enumerate(distance):
        #print(d_travel - distance[i])
        if d_travel - distance[i] < 0:
            print(-1)
            break
        
        elif d_travel - distance[i] < tank and smallest > d_travel - distance[i]:
            print(distance[i])
            stops += 1
            
    print(distance)
    distance = distance[i:]
    print(distance)
    if len(distance) == 1:
        print(stops)
        break

  
    n -= 1
   




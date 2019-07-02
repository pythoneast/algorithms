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


max_stops = 4
tank = 400
stations =[200,375,500,700]
distance = []

for station in stations:
    x = 400 - station
    distance.append([x,station])


least = distance[0][0]
for i,v in enumerate(distance):
    #least = distance[i][0]
    
    #this is the first move
    if least > distance[i][0] and distance[i][0]>0:
        least = i
        
#miles traveled       
miles = tank + stations[least]

#want to forget about the rest of the distances
distance = distance[least +1:]
stations = stations[least+1:]
for i, v in enumerate(distance):
    if least > distance[i][0] +miles and distance[i][0]>0:
        least = i
print(stations[least], "final")

print(miles, "miles")

'''
y = 400 + 375
print(y)
print(y -100)
print(y - 300)

'''

if __name__ == '__main__':
    print(compute_min_refills(950,400,[200,375,550,750]))
    #print(compute_min_refills(10,3,[1,2,5,9]))
    #d, m, _, *stops = map(int, sys.stdin.read().split())
    #print(compute_min_refills(d, m, stops))
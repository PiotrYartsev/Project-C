#make a 1D random walker

#make an array of 1000 zeros

from operator import index
from matplotlib import patches
import numpy as np
import matplotlib.pyplot as plt
import random

from sklearn.decomposition import randomized_svd

#make an array of 1000 zeros
size=50
number_of_balls=20
#make 2d array
x = np.zeros((size,size))

#radnomly distribute 100 1s
p=0
while p < number_of_balls:
    i=random.randint(0, size-1)
    j=random.randint(0, size-1)
    x[i][j] = 1
    p+=1


where_points=[]

for i in range(len(x)):
    for j in range(len(x[i])):
        if x[i][j] == 1:
            where_points.append([i,j])
            
print(where_points)




what_happened=[]
def run_this_code(where_points):
    n=number_of_balls
    print(n)
    resulting_points=[]
    #shoose to move left or right
    number_of_steps=0
    while n > 1:
        i=random.choice(range(len(where_points)))
        print(len(where_points))
        print(i)
        x=where_points[i][0]
        y=where_points[i][1]
        #print(x)
        #print(y)
        randomvar=np.random.random()
        #go to the left
        if randomvar < 1/4:
            #if you cant go to the left die
            if x-1 < 0:
                what_happened.append([where_points[i],1])
                del where_points[i]

                
            else:
                #print(where_points[i][0])
                where_points[i][0] -= 1
                if where_points.count(where_points[i]) > 1:
                    what_happened.append([where_points[i],1])
                    where_points=list(filter(lambda a: a != where_points[i], where_points))
    
                    

                else:
                    what_happened.append([[0,0],-1])
        
        #go to the right
        if randomvar < 2/4:
            #if you cant go to the right die
            if x+1 > size:
                what_happened.append([where_points[i],1])
                del where_points[i]

                
            else:
                where_points[i][0] += 1
                if where_points.count(where_points[i]) > 1:
                    what_happened.append([where_points[i],1])
                    where_points=list(filter(lambda a: a != where_points[i], where_points))
    

                else:
                    what_happened.append([[0,0],-1])
        
        #go up
        if randomvar < 3/4:
            #if you cant go to the right die
            if y+1 > size:
                what_happened.append([where_points[i],1])
                del where_points[i]

                
            else:
                where_points[i][1] += 1
                if where_points.count(where_points[i]) > 1:
                    what_happened.append([where_points[i],1])
                    where_points=list(filter(lambda a: a != where_points[i], where_points))
    
                    

                else:
                    what_happened.append([[0,0],-1])
        
        #go down
        if randomvar < 4/4:
            #if you cant go to the right die
            if y-1 < 0:
                what_happened.append([where_points[i],1])
                del where_points[i]

                
            else:
                #print(where_points[i][1])
                where_points[i][1] -= 1
                if where_points.count(where_points[i]) > 1:
                    what_happened.append([where_points[i],1])
                    where_points=list(filter(lambda a: a != where_points[i], where_points))
    





                    

                else:
                    what_happened.append([[0,0],-1])

    
        where_points=sorted(where_points)
        where_points2=where_points.copy()
        resulting_points.append(where_points2)        
        if len(where_points)==n:
            print(where_points)
            pass
        else:
            n=len(where_points)
            #print(n)
        
    number_of_steps+=1
    return resulting_points, number_of_steps, what_happened
run_this_code(where_points)
"""
resulting_points,number_of_steps,what_happened=run_this_code(where_points)

print(number_of_steps)

onec=[]
for k in resulting_points:
onec.append([1]*len(k))"""


#make a 1D random walker

#make an array of 1000 zeros

from operator import index
from matplotlib import patches
import numpy as np
import matplotlib.pyplot as plt
import random

#make an array of 1000 zeros
size=50
number_of_balls=20
x = np.zeros(size)

#radnomly distribute 100 1s
while sum(x) < number_of_balls:
    x[random.randint(0, size-1)] = 1

where_points=[]
for i in range(len(x)):
    if x[i] == 1:
        where_points.append(i)

print(where_points)



what_happened=[]
def run_this_code(where_points):
    n=number_of_balls
    resulting_points=[]
    #shoose to move left or right
    number_of_steps=0
    while n > 1:
        i=random.choice(range(len(where_points)))
        #print(i)
        #if less then 0.5 go to the left
        if np.random.random() < 0.5:
            #if you cant go to the left die
            if i-1 < 0:
                what_happened.append([where_points[i],1])
                del where_points[i]
                
            else:
                where_points[i] -= 1
                if where_points.count(where_points[i]) > 1:
                    what_happened.append([where_points[i],1])
                    where_points=list(filter(lambda a: a != where_points[i], where_points))
                    

                else:
                    what_happened.append([0,-1])


                
        else:
            #if you cant go to the right die
            if i+1 > size:
                what_happened.append([where_points[i],1])
                del where_points[i]
                
            else:
                where_points[i] += 1
                if where_points.count(where_points[i]) > 1:
                    what_happened.append([where_points[i],1])
                    where_points=list(filter(lambda a: a != where_points[i], where_points))
                    
                else:
                    what_happened.append([0,-1])
                    

        
                
        where_points=sorted(where_points)
        where_points2=where_points.copy()
        resulting_points.append(where_points2)
        if len(where_points)==n:
            #print(where_points)
            pass
        else:
            n=len(where_points)
            #print(n)
            
        number_of_steps+=1
    return resulting_points, number_of_steps, what_happened
"""
resulting_points,number_of_steps,what_happened=run_this_code(where_points)

print(number_of_steps)

onec=[]
for k in resulting_points:
    onec.append([1]*len(k))


#plot the array
#plt.plot(x)
#plt.show()


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
fig, ax = plt.subplots()
ax.set_xlim(-0.6, size+0.6)
ax.set_ylim(0.4, 1.6)
ax.set_title('Random Walker')
ax.set_xlabel('Position')
ax.set_ylabel('Occupied')
#Set size of plot
fig.set_size_inches(15, 2)

#set up lines seperating the bins
for i in range(size+2):
    plt.axvline(i-0.5, color='k', linestyle='--', linewidth=1)


# set up empty lines to be updates later on
l1, = ax.plot([],[],'bo ')
l2, = ax.plot([],[],'ro')

def gen1():
    i = 0
    while(i<len(resulting_points)):
        yield i
        i += 1

def run1(c):
    l1.set_data(resulting_points[c], onec[c])
    l2.set_data(what_happened[c][0],what_happened[c][1])

#slow down the animation
ani1 = animation.FuncAnimation(fig,run1,gen1,interval=100,blit=False,repeat=False)
#ani2 = animation.FuncAnimation(fig,run2,gen2,interval=100,blit=False,repeat=False)
plt.show()
#save the ani1 and ani2 as a gif

ani1.save('random-walker.gif', fps=3,writer='imagemagick')"""


plot_number_of_steps=[]
for n in range(50000):
    size=50
    number_of_balls=20
    x = np.zeros(size)

    #radnomly distribute 100 1s
    while sum(x) < number_of_balls:
        x[random.randint(0, size-1)] = 1

    where_points=[]
    for i in range(len(x)):
        if x[i] == 1:
            where_points.append(i)


    what_happened=[]
    resulting_points,number_of_steps,what_happened=run_this_code(where_points)
    plot_number_of_steps.append(number_of_steps)

plt.hist(plot_number_of_steps, bins=30)
plt.show()


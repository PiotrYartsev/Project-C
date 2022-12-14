#make a 1D random walker

#make an array of 1000 zeros

import random
from operator import index
from certifi import where

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import patches
from pandas import array
from tqdm import tqdm

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
            if where_points[i]-1 < 0:
                what_happened.append([where_points[i],1])
                del where_points[i]
                
            else:
                
                where_points.append((where_points[i]-1))
                del where_points[i]
                if len(list(set(where_points)))!=len(where_points):
                    what_happened.append([where_points[-1],1])
                    #delete all examples of points that are the same
                   #print(len(where_points))    
                    where_points = [x for x in where_points if where_points.count(x) == 1]
                   #print(len(where_points))
                    
                    

                else:
                    what_happened.append([0,-1])


                
        else:
            #if you cant go to the right die
            if where_points[i]+1 > size:
                what_happened.append([where_points[i],1])
                del where_points[i]
                
            else:
                
                where_points.append((where_points[i]+1))
                del where_points[i]
                if len(list(set(where_points)))!=len(where_points):
                    what_happened.append([where_points[-1]+1,1])

                    where_points = [x for x in where_points if where_points.count(x) == 1]
                    

                else:
                    what_happened.append([0,-1])
                    

        
                
        values=str(where_points)

        resulting_points.append(values)
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




second_resulting_points=[]
for i in range(len(resulting_points)):
    newstuff=resulting_points[i][1:-1]
    newstuff=newstuff.split(',')

    newstuff=[int(i) for i in newstuff]
    second_resulting_points.append(newstuff)


resulting_points=second_resulting_points


onec=[]
for k in resulting_points:
    onec.append([1]*len(k))

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ax.set_xlim(-0.6, size+0.6)
ax.set_ylim(0.4, 1.6)
ax.set_title('Random Walker: 1D' )
ax.set_xlabel('Position')
ax.set_ylabel('Occupied')
#remove y axis
ax.axes.get_yaxis().set_visible(False)

#Set size of plot
fig.set_size_inches(15, 2)

#set up lines seperating the bins
for i in range(size+2):
    plt.axvline(i-0.5, color='k', linestyle='--', linewidth=1)
plt.axvline(-0.5, color='r', linestyle='-', linewidth=1, label='"kill" bondary')
plt.axvline(size+0.5, color='r', linestyle='-', linewidth=1)


# set up empty lines to be updates later on
l1, = ax.plot([],[],'bo')
l2, = ax.plot([],[],'ro')
#write the number of balls each frame



def gen1():
    i = 0
    while(i<len(resulting_points)):
        yield i
        i += 1

def run1(c):
    l1.set_data(resulting_points[c], onec[c],)
    l2.set_data(what_happened[c][0],what_happened[c][1])
    ax.set_title('Random Walker: 1D, Step: '+str(c))
    l1.set_label('Number of balls: '+str(len(resulting_points[c])))
    ax.legend(loc='upper right')
    
    
#slow down the animation
ani1 = animation.FuncAnimation(fig,run1,gen1,interval=450,blit=False,repeat=False)

plt.show()
#save the ani1 and ani2 as a gif

ani1.save('random-walker-1D.gif', fps=1,writer='imagemagick')


"""
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
plot_number_of_steps=[]
x22=[]
y=[]
numberofsteps=1
for n in tqdm(range(numberofsteps)):
    size=1000
    number_of_balls=size*0.4
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
    for i in range(len(resulting_points)):
        y.append(i)
        x22.append(len(resulting_points[i]))




plt.plot(x22,y,'bo',label="Population at time t",markersize=1)
plt.xlabel("Time t")
plt.ylabel("Density of balls")
plt.legend()
x=array(x22)
y=array(y)


def func(x, a):
    return a * x**(-1/2)

popt, pcov = curve_fit(func, x, y)
print(popt)
print(pcov)
plt.plot(x, func(x, *popt), 'r-',label="Fitted function")



#set log scale
plt.yscale('log')


plt.show()
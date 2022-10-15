#make a 1D random walker

#make an array of 1000 zeros

from operator import index, le
from matplotlib import patches
import numpy as np
import matplotlib.pyplot as plt
import random

from sklearn.decomposition import randomized_svd

#make an array of 1000 zeros
size=10
number_of_balls=10
#make 2d array
x1 = np.zeros((size,size))

#radnomly distribute 100 1s
p=0
while p < number_of_balls:
    i=random.randint(0, size-1)
    j=random.randint(0, size-1)
    x1[i][j] = 1
    p+=1


where_points=[]

for i in range(len(x1)):
    for j in range(len(x1[i])):
        if x1[i][j] == 1:
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
        before=where_points[:]
        x=where_points[:][i][0]
        y=where_points[:][i][1]
        #print(x)
        #print(y)
        randomvar=np.random.random()
        
        #go to the left
        if randomvar < 1/4:
            #print("left")
            #if you cant go to the left die
            if x-1 < 0:
                #print("left die")
                what_happened.append([where_points[i],1])
                del where_points[i]

                
            else:

                where_points[i][0] = where_points[:][i][0]-1

                if where_points.count(where_points[i]) > 1:

                    what_happened.append([where_points[i],1])
                    where_points=list(filter(lambda a: a != where_points[i], where_points[:]))
                    

                else:
                    what_happened.append([[0,0],-1])
        
        #go to the right
        if randomvar < 2/4 and randomvar > 1/4:
            #if you cant go to the right die
            if x+1 > size:
                what_happened.append([where_points[i],1])
                del where_points[i]

                
            else:

                where_points[i][0] = where_points[:][i][0]+1


                if where_points.count(where_points[i]) > 1:
                    what_happened.append([where_points[i],1])
                    where_points=list(filter(lambda a: a != where_points[i], where_points[:]))
    

                else:
                    what_happened.append([[0,0],-1])
        
        #go up
        if randomvar < 3/4 and randomvar > 2/4:
            #if you cant go to the right die
            if y+1 > size:
                what_happened.append([where_points[i],1])
                del where_points[i]

                
            else:

                where_points[i][1] = where_points[:][i][1]+1

                if where_points.count(where_points[i]) > 1:
                    what_happened.append([where_points[i],1])

                    where_points=list(filter(lambda a: a != where_points[i], where_points[:]))


                    

                else:
                    what_happened.append([[0,0],-1])
        
        #go down
        if randomvar < 4/4 and randomvar > 3/4:
            #if you cant go to the right die
            if y-1 < 0:
                what_happened.append([where_points[i],1])
                del where_points[i]

                
            else:

                where_points[i][1] = where_points[:][i][1]-1

                if where_points.count(where_points[i]) > 1:
                    what_happened.append([where_points[i],1])
                    #print(len(where_points))
                    where_points=list(filter(lambda a: a != where_points[i], where_points[:]))
                    #print(len(where_points))





                    

                else:
                    what_happened.append([[0,0],-1])

        
        
        
        #print(len(where_points))
        if len(where_points)==n:
            pass
        else:    
            n=len(where_points)
            print(n)
        #append the value of a list
        resulting_points.append(where_points[:])

            
        
        number_of_steps+=1
    return resulting_points, number_of_steps, what_happened

resulting_points,number_of_steps,what_happened=run_this_code(where_points)
print(number_of_steps)
#print the values in the same list I appended to before






import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
fig, ax = plt.subplots()

ax.set_title('Random Walker')
ax.set_xlabel('Position in x')
ax.set_ylabel('Position in y')
#Set size of plot
fig.set_size_inches(15, 2)

#set up lines seperating the bins
for i in range(size+2):
    plt.axvline(i-0.5, color='k', linestyle='--', linewidth=1)
    plt.axhline(i-0.5, color='k', linestyle='--', linewidth=1)


# set up empty lines to be updates later on
l1, = ax.plot([],[],'bo ')
l2, = ax.plot([],[],'ro')

def gen1():
    i = 0
    while(i<len(resulting_points)):
        yield i
        i += 1



def run1(c):
    print(c)
    x=[o[0] for o in resulting_points[c]]
    
    y=[o[1] for o in resulting_points[c]]

    l1.set_data(x,y)
    #l2.set_data(what_happened[c][0],what_happened[c][1])


#slow down the animation
ani1 = animation.FuncAnimation(fig,run1,gen1,interval=10,blit=False,repeat=False)
#ani2 = animation.FuncAnimation(fig,run2,gen2,interval=100,blit=False,repeat=False)
plt.show()
#save the ani1 and ani2 as a gif

#ani1.save('random-walker.gif', fps=3,writer='imagemagick')"""
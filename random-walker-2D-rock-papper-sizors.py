#make a 1D random walker

#make an array of 1000 zeros

import random
from cProfile import label
from operator import index, le

import matplotlib.pyplot as plt
import numpy as np
from joblib import PrintTime
from matplotlib import patches
from matplotlib.cbook import get_sample_data
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
from scipy import rand
from sklearn.decomposition import randomized_svd
from sympy import N
from tqdm import tqdm

#make an array of 1000 zeros
size=6
number_of_balls=20
#make 2d array
x1 = np.zeros((size,size))

#radnomly distribute 100 1s
p=0
while p < number_of_balls:
    i=random.randint(0, size-1)
    j=random.randint(0, size-1)
    x1[i][j] = 1
    p+=1


where_points_rock=[]
where_points_paper=[]
where_points_sizors=[]

for i in range(len(x1)):
    for j in range(len(x1[i])):
        if x1[i][j] == 1:
            randomvar=np.random.random()
            if randomvar < 1/3:
                where_points_rock.append([i,j])
            elif randomvar < 2/3 and randomvar > 1/3:
                where_points_paper.append([i,j])
            else:
                where_points_sizors.append([i,j])
            
            
print("rock")
print(where_points_rock)
print("paper")
print(where_points_paper)
print("sizors")
print(where_points_sizors)


resulting_points2=[]






def choose_point_and_direction(list_to_choose_from):
    #choose_point
    i=random.choice(range(len(list_to_choose_from)))
    #choose direction
    randomvarformove=np.random.random()
    if randomvarformove < 1/4:
        direction=[1,0]
    elif randomvarformove < 2/4 and randomvarformove > 1/4:
        direction=[-1,0]
    elif randomvarformove < 3/4 and randomvarformove > 2/4:
        direction=[0,1]
    else:
        direction=[0,-1]

    return(list_to_choose_from[i],direction)






def moving_and_shecking(new_position,you,beatyou,youbeat,direction,size):

    #if the postion has to be deleted set it to none
    #if position is not changed, set it to False
    #if the position of the where the ball move is added to your collection, set it to True. 


    #if the new position is not in the list of all points, delete the ball
    if new_position[0] < 0 or new_position[0] > size-1 or new_position[1] < 0 or new_position[1] > size-1:
        return("delete")
    #if it is a valid move sheck where it is moving
    else:
        #check if coinsides with itself
        if new_position in you:
            #dont move
            return("dont move")
            
        #does it beat you
        if new_position in beatyou:
            #delete the ball, add it to position of who beat you
            return("die")
        
        #do you beat it
        if new_position in youbeat:
            return("win")
        #no one there, move
        else:
            return("move")










newrock=[]
newpaper=[]
newsizors=[]
def run_this_code(where_points_rock,where_points_paper,where_points_sizors,all_points,limit):

    #shoose to move left or right
    number_of_steps=0
    while number_of_steps < limit and len(where_points_rock)+len(where_points_paper)+len(where_points_sizors) > 0:
        size=len(all_points)
        total=len(where_points_rock)+len(where_points_paper)+len(where_points_sizors)
        randomvar=np.random.random()

        #rock
        if randomvar < len(where_points_rock)/total:
            #print("rock")
            
            point,direction=choose_point_and_direction(where_points_rock)
            newpoint=[point[0]+direction[0],point[1]+direction[1]]
            result =(moving_and_shecking(newpoint,where_points_rock,where_points_paper,where_points_sizors,direction,size))
            if result=="delete":
                where_points_rock.remove(point)
            elif result=="dont move":
                pass
            elif result=="die":
                try:
                    where_points_rock.remove(point)
                    where_points_paper.append(newpoint)
                except:
                    raise Exception("die",newpoint,where_points_paper)
            elif result=="win":
                try:
                    where_points_rock.append(newpoint)
                    where_points_sizors.remove(newpoint)
                except:
                    raise Exception("win",newpoint,where_points_sizors)
            elif result=="move":
                try:
                    where_points_rock.remove(point)
                    where_points_rock.append(newpoint)
                except:
                    raise Exception("move",newpoint,where_points_rock)

            
            
                
                        
                




        #paper
        elif randomvar < len(where_points_rock)/total+len(where_points_paper)/total and randomvar > len(where_points_rock)/total:

            #print("paper")
            point,direction=choose_point_and_direction(where_points_paper)
            #print(point)
            newpoint=[point[0]+direction[0],point[1]+direction[1]]
            result =(moving_and_shecking(newpoint,where_points_paper,where_points_sizors,where_points_rock,direction,size))
            if result=="delete":
                where_points_paper.remove(point)
            elif result=="dont move":
                pass
            elif result=="die":
                try:
                    where_points_paper.remove(point)
                    where_points_sizors.append(newpoint)
                except:
                    raise Exception("die",newpoint,where_points_sizors)
            elif result=="win":
                try:
                    where_points_paper.append(newpoint)
                    where_points_rock.remove(newpoint)
                except:
                    raise Exception("win",newpoint,where_points_rock)

            elif result=="move":
                try:
                    where_points_paper.remove(point)
                    where_points_paper.append(newpoint)
                except:
                    raise Exception("move",newpoint,where_points_paper)







        #sizors
        else:
            #print("sizors")

            point,direction=choose_point_and_direction(where_points_sizors)
            #print(point)
            newpoint=[point[0]+direction[0],point[1]+direction[1]]
            result=(moving_and_shecking(newpoint,where_points_sizors,where_points_rock,where_points_paper,direction,size))
            if result=="delete":
                where_points_sizors.remove(point)
            elif result=="dont move":
                pass
            elif result=="die":
                try:
                    where_points_sizors.remove(point)
                    where_points_rock.append(newpoint)
                except:
                    raise Exception("die",newpoint,where_points_rock)

            elif result=="win":
                try:

                    where_points_sizors.append(newpoint)
                    where_points_paper.remove(newpoint)
                except:
                    raise Exception("win",newpoint,where_points_paper)

            elif result=="move":
                try:
                    where_points_sizors.remove(point)
                    where_points_sizors.append(newpoint)
                except:
                    raise Exception("move",newpoint,where_points_sizors)
        
        number_of_steps+=1

        
        newrock.append(str(where_points_rock[:]))
        newpaper.append(str(where_points_paper[:]))
        newsizors.append(str(where_points_sizors[:]))
    return(number_of_steps)


"""

run_this_code(where_points_rock,where_points_paper,where_points_sizors,x1)
"""
def str_to_list(resulting_points):
    second_resulting_points=[]
    for i in range(len(resulting_points)):
        if resulting_points[i]=="[]":
            second_resulting_points.append([])
        else:
            newstuff=resulting_points[i][1:-1]
            newstuff=newstuff.split("], [")
            
            newlist=[]
            for j in range(len(newstuff)):
                newstuff2=newstuff[j].replace("]","")
                newstuff2=newstuff2.replace("[","")
                newstuff2=newstuff2.split(", ")
                newstuff2[0]=int(newstuff2[0])
                newstuff2[1]=int(newstuff2[1])
                newlist.append(newstuff2)
            second_resulting_points.append(newlist)

    return(second_resulting_points)
"""
newrock=str_to_list(newrock)
newpaper=str_to_list(newpaper)
newsizors=str_to_list(newsizors)

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

ax.set_title('Rock/Paper/Sizors: 2D')
ax.set_xlabel('Position in x')
ax.set_ylabel('Position in y')
#Set size of plot
fig.set_size_inches(15, 15)

#set up lines seperating the bins
for i in range(size+2):
    plt.plot([i-0.5,i-0.5],[0-0.5,size+1-0.5],color="black",linewidth=1,linestyle="--")
    plt.plot([0-0.5,size+1-0.5],[i-0.5,i-0.5],color="black",linewidth=1,linestyle="--")
plt.plot([-0.5,-0.5],[size+0.5,-0.5],color='r', linestyle='-', linewidth=1,label="Deadly border")
plt.plot([size+0.5,-0.5],[size+0.5,size+0.5],color='r', linestyle='-', linewidth=1)
plt.plot([size+0.5,size+0.5],[size+0.5,-0.5],color='r', linestyle='-', linewidth=1)
plt.plot([size+0.5,-0.5],[-0.5,-0.5],color='r', linestyle='-', linewidth=1)


# set up empty lines to be updates later on
rock, = ax.plot([],[],'b*',label="Rock")
paper, = ax.plot([],[],'r+',label="Paper")
sizors, = ax.plot([],[],'go',label="Sizors")

def gen1():
    i = 0
    while(i<len(newrock)):
        yield i
        i += 1



def run1(c):
    #print(c)
    x_r=[o[0] for o in newrock[c]]
    
    y_r=[o[1] for o in newrock[c]]

    rock.set_data(x_r,y_r)

    x_p=[o[0] for o in newpaper[c]]
    y_p=[o[1] for o in newpaper[c]]
    paper.set_data(x_p,y_p)

    x_s=[o[0] for o in newsizors[c]]
    y_s=[o[1] for o in newsizors[c]]
    sizors.set_data(x_s,y_s)


    #l2.set_data(what_happened[c][0],what_happened[c][1])

plt.legend(loc="upper left")
#slow down the animation
ani1 = animation.FuncAnimation(fig,run1,gen1,interval=400,blit=False,repeat=False)
#ani2 = animation.FuncAnimation(fig,run2,gen2,interval=100,blit=False,repeat=False)
plt.show()
#save the ani1 and ani2 as a gif

ani1.save('plots/rock-paper_sizors.gif', fps=3,writer='imagemagick')
"""

plot_number_of_steps_rock=[]
plot_number_of_steps_paper=[]
plot_number_of_steps_sizors=[]
numberofsteps=10000
for n in tqdm(range(numberofsteps)):
    #make an array of 1000 zeros
    size=10
    number_of_balls=40
    #make 2d array
    x1 = np.zeros((size,size))

    #radnomly distribute 100 1s
    p=0
    while p < number_of_balls:
        i=random.randint(0, size-1)
        j=random.randint(0, size-1)
        x1[i][j] = 1
        p+=1
    

    where_points_rock=[]
    where_points_paper=[]
    where_points_sizors=[]

    for i in range(len(x1)):
        for j in range(len(x1[i])):
            if x1[i][j] == 1:
                randomvar=np.random.random()
                if randomvar < 1/3:
                    where_points_rock.append([i,j])
                elif randomvar < 2/3 and randomvar > 1/3:
                    where_points_paper.append([i,j])
                else:
                    where_points_sizors.append([i,j])
    newrock=[]
    newpaper=[]
    newsizors=[]     
    newrock=str_to_list(newrock)
    newpaper=str_to_list(newpaper)
    newsizors=str_to_list(newsizors)


    limit=400
    number_of_steps=run_this_code(where_points_rock,where_points_paper,where_points_sizors,x1,limit)
    
    plot_number_of_steps_rock.append(len(newrock[-1]))
    plot_number_of_steps_paper.append(len(newpaper[-1]))
    plot_number_of_steps_sizors.append(len(newsizors[-1]))
    


numberofbins=int(len(list(set(plot_number_of_steps_rock)))/2)
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(15,5))
axes[0].hist(plot_number_of_steps_rock,color="r", bins=numberofbins,label="Number of\nrocks left".format(number_of_balls))
axes[1].hist(plot_number_of_steps_paper,color="b", bins=numberofbins,label="Number of\npapers left".format(number_of_balls))
axes[2].hist(plot_number_of_steps_sizors,color="g", bins=numberofbins,label="Number of\nsizors left".format(number_of_balls))
fig.tight_layout()


axes[0].legend()
axes[1].legend()
axes[2].legend()

fig.supxlabel('Number of steps')
fig.supylabel('Number of times')
fig.suptitle('Number of items after {} iterations'.format(limit))
#plt.show()
plt.tight_layout()
plt.savefig('plots/rock-paper-sizors-after-{}.png'.format(limit))

#"""
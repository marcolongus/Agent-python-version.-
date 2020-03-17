import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from classparticle import *
import matplotlib.patches as patches

######################################################################
#Cargamos data
######################################################################


data = np.loadtxt("evolution.txt",usecols=(0,1), unpack=True)

a_estados = np.loadtxt("estados.txt",usecols=0, unpack=True)

array =np.loadtxt("array.txt",usecols=(0,1), unpack=True)

x=np.loadtxt("array.txt", usecols=0)
y=np.loadtxt("array.txt", usecols=1)

grafico1 = np.loadtxt('array.txt')

######################################################################
#Definimos fig
######################################################################

fig1 = plt.figure()
ax1 = fig1.add_axes([0.1,0.1,0.8,0.8])

l, = ax1.plot([],[],'o')


plt.title("Obstacles configuration") 
plt.xlabel("x axis") 
plt.ylabel("y axis")

plt.axis('square')

plt.xlim(-1,L+1)
plt.ylim(-1,L+1)

plt.grid(color='b', linestyle='-.', linewidth=0.5)


######################################################################
#iniciamos la animación
######################################################################


def update_line(num, data, line):


    line.set_data(data[..., num-1:num+N])
    if(num%N==0):
    	line.set_color('red')
    else:
    	line.set_color('blue')
    

    return line,

line_ani = animation.FuncAnimation(fig1, update_line, frames=9999, fargs=(data, l), interval=0.1, blit=True)

plt.show()




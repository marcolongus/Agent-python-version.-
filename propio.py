import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from classparticle import *
import matplotlib.patches as patches

##############################################################################################
#Animacion
##############################################################################################

def trayectoria(np_steps,tpause=0.01):

	fig, ax = plt.subplots()

	for i in range(np_steps):

		x = np.loadtxt("evolution.txt",usecols=0, skiprows=N*i, max_rows=N)
		y = np.loadtxt("evolution.txt",usecols=1, skiprows=N*i, max_rows=N)

		estado = np.loadtxt("estados.txt",usecols=0, skiprows=N*i, max_rows=N,dtype=int)
				
		plt.cla()

		plt.title("Agents system") 
		plt.xlabel("x coordinate") 
		plt.ylabel("y coordinate")

		plt.axis('square')
		plt.grid()
		plt.xlim(-1,L+1)
		plt.ylim(-1,L+1)

		for j in range(N):
			circ = patches.Circle((x[j],y[j]), 1, alpha=0.7, fc= colores[estado[j]])
			ax.add_patch(circ)

		#plt.plot(x,y,'o',color='red')
		#plt.savefig("test_rasterization%i.png" %(i), dpi=150)
		plt.pause(tpause)

##################################################################################################



trayectoria(300)



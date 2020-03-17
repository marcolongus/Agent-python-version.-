import numpy as np
import matplotlib.pyplot as plt
import sortedcontainers as st

#########################################################################
#Constantes del sistema
#########################################################################

#Variables

N=15
L=20

time_f = 300

delta_time = 1.
active_vel= 0.2

#Fijas

infinity = 10000000000000000
gamma_friction = 3.92*active_vel
radius =1.
diameter = 2*radius
dos_pi = 2*np.pi


tau_t=1. 
p_transmision = (1./tau_t)*delta_time #sane---->infected 

tau_i=14.
p_infection   = (1./tau_i)*delta_time #infected--->refractary 

tau_r=60.
p_recfractary = (1./tau_r)*delta_time #refractary--->sane

alpha=100.
p_rotation    = (1./alpha)*delta_time 


#Para graficar, azul sano, rojo infectado y verde recuperado. 

colores = ['blue','red', 'green', ]

#########################################################################
#Arregla el problema de la indexación de numpy
#########################################################################

class elemento(object):

	def  __init__(self,set=st.SortedSet):
		self.set = st.SortedSet()


#########################################################################
#Clase Particle
#########################################################################

class Particle(object):

#Métodos
	
	def __init__(self,x=np.zeros(2),angle=0,velocity=active_vel, node=np.zeros(2),state=int):

		self.x = x		
		self.angle = angle
		self.velocity = velocity
		self.node = x.astype(int)
		self.state = state

	#Método par actualizar el nodo:	
	def nodo(self):
		self.node= np.mod(self.x.astype(int),L)

	#Metodo para acutalizar estado:
	def estado(self,a=int):
		self.state = a	

#Funciones

#Funciones de epidemia
def sane(A):		
	return A.state==0

def infected(A):		
	return A.state==1

def refractary(A):		
	return A.state==2

def create_particle():
	A = Particle(np.random.uniform(size=2)*L,np.random.uniform()*dos_pi, state=np.random.randint(0,3))
	return A

def dx_distance(A=Particle,B=Particle):
	
	res = infinity
	dy = np.zeros(2)
	res_x = infinity
	res_y = infinity
	dx=np.zeros(shape=(3,2))

	for i in range(-1,2):
		x  = A.x + i*L		
		dx[i+1] = x - B.x

		if ( np.abs(dx[i+1][0]) < res_x ):
			dy[0]=dx[i+1][0]
			res_x=abs(dy[0])

		if ( np.abs(dx[i+1][1]) < res_y ):
			dy[1]=dx[i+1][1]
			res_y=abs(dy[1])	

	dis = np.sqrt((np.square(dy).sum()))

	if (dis <= diameter):
		inter = True
	else:
		inter = False

	result = np.append(dy,np.array([dis]))

	return result


def evolution(system=np.array, part_index=int, box=np.array ,dtype=np.object):
	
	#Creamos partícula evolucionada en el tiempo.
	#box contiene los índices de las partículas con las que puede ser que interactue.
	#part_index es el índice de la partícula que estamos evolucionando.


	A = Particle() #Partícula por defecto en el origin con A.vel=active_vel
	A.angle = system[part_index].angle	
	A.x = system[part_index].x.copy()
	A.state = system[part_index].state

	potencial = np.zeros(2)
	campo = np.zeros(2)

	inter_set = st.SortedSet() #Guardamos la partículas que interactúan

	interact=False

	#Loop sobre todas las partículas que interactúa:

	for i in range(5):
		for j in range(5):

			for particles in box[i,j].set:

				if (particles != part_index):
					dx = dx_distance(system[part_index],system[particles])

					if(dx[2] <= diameter):
						interact=True		
						
						inter_set.add(particles)

						#calculamos potencial
						distance = np.square(dx[0:2]).sum()
						distance = np.sqrt(distance)
						potencial += np.power(distance,-3)*dx[0:2]
						potencial *= gamma_friction	

	#############################################################################

	if (interact):
		#Calculo del campo resultante
		field = np.array([np.cos(system[part_index].angle), np.sin(system[part_index].angle)])
		field *=active_vel
		field +=potencial 
						
		#Evolución		
		A.x += delta_time*field
		A.x = np.mod(A.x,L)
	
	else:
		#print(dx, dx.shape, "no interact")
		vel = active_vel*np.array([np.cos(system[part_index].angle), np.sin(system[part_index].angle)])		
		A.x += delta_time*vel
		A.x = np.mod(A.x,L)
	
	#Actualizamos el nodo de la evolución
	A.nodo()
	

	#Evolución de la epidemia:
	
	flag = True

	for particle in inter_set:

		if (sane(A) and infected(system[particle])):
			if (np.random.rand(1) < p_transmision):
				A.estado(1)
				flag=False

		if (refractary(A) and np.random.rand(1)<p_recfractary):
			A.estado(0)


		if(infected(A) and flag):
			if (np.random.rand(1)<p_infection):
				A.estado(2)

	return A


#########################################################################











import numpy as np
from classparticle import *

def cambio(A=Particle, dtype= np.object):
	B = Particle()
	print("B: ",B.x, B.velocity, B.node,B.angle),print()
	B.x = A.x.copy()	
	B.x+=1
	B.nodo()	
	return B


file = open("random.txt","w")



A = Particle(angle=np.pi)
A.x += 1.1 

print(A.x)


C = cambio(A)

print(A.x, A.node, A.angle)
print(C.x, C.node, C.angle)

file.close()

a=np.array([1])
b=a
b=np.array([2])
b[0]=a[0]
a[0]=5

print(a,b)
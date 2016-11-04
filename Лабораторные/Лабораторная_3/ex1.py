from math import sqrt
from sympy import *
import numpy as np
# import matplotlib.pyplot as plt
from pylab import *

ex=[[1300,0.7],[1300,0.6],[1700,0.5],[1700,0.65]]
# B=6.36*10**(-5)
B=(0.186*10**-5)*0.342
L=0.163
dU=62.6
dK=0.001
summ=0
dS=0
a=[0,0,0,0]
i=0
for element in ex:
	U_a=element[0]
	# print(U_a,B,L)
	K=element[1]/100
	eta=(8*(K**2)*U_a)/((B**2)*(L**4))
	# dS=(8/((B**2)*(L**4)))*sqrt((U_a*2*K*dK)**2+(K**2*dU)**2)
	dEta=(2*dK)/(K)+(dU)/(U_a)*0.01
	a[i]=dEta*eta
	i+=1
	dS+=eta*dEta
	summ+=eta
	# print()
# print(dS/4)	
# print(summ/4)

def function(K):
	return (((B**2)*(L**4)*(1.75*(10**11)))/K**2)*1000

K=np.linspace(0.005, 0.01, 20) 

U=function(K)
print(U,K)
plot( U, K, "-", color='black', linewidth = 1.3)
grid(True)

i=0
# ex=[ex[0]]
for element in ex:
	dUU=a[i]
	i+=1
	U_a=element[0]
	K_=element[1]/100
	plot(U_a,K_, "o", color='black')
	print(U_a+dU,K_+dK)
	gca().add_patch(Rectangle((U_a-dU,K_-dK),(dU)*2,(dK)*2, color="grey"))

rc('text', usetex=True)
rc('font', family='Droid Sans')
rc('text.latex',unicode=True)
rc('text.latex',preamble=r'\usepackage[utf8]{inputenc}')
rc('text.latex',preamble=r'\usepackage[russian]{babel}')

ylabel(r'$K$, м')

xlabel(r'$U_a$, В')
show()


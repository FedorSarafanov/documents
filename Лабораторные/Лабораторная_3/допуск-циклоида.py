# import matplotlib as mpl
# from mpl_toolkits.mplot3d import Axes3D
import numpy as np
# import matplotlib.pyplot as plt
from math import * 

# from sympy import *


# mpl.rcParams['legend.fontsize'] = 10

# fig = plt.figure()
# ax = fig.gca(projection='3d')

# Константы

n0=8400				# Плотность намотки
mu0=4*pi*(10**(-7)) # Магнитная постоянная
eta=1.74*(10**11)	# Известное e/m

# Переменные

dl=0.016 	# Длина пластин
d=0.0055 	# Расстояние между пластинами
D=0.07		# Диаметр соленоида

U_a=1200	# Напряжение второго анода
I=30*0.02	# Ток на соленоиде
U=75		# Эффективное напряжение на пластинах

B=mu0*n0*I 			# Индукция в соленоиде
omega=eta*B			# Циклотронная частота
v0z=sqrt(eta*2*U_a)	# Время пролета в пластинах
tau=dl/V0z 			# Время пролета в пластинах
E=75/dl				# Напряженность в пластинах


tau2=(l-D)/v0z+(3.7*10**(-9))
print('tau2',tau2)
# phi=pi

# D=E/(omega*B)

# z=np.arange(0,0.014,0.0001)

# def x(z):
# 	return D*(1-np.cos(omega*z/v0z))

# def y(z):
# 	return D*(np.sin(omega*z/v0z)-omega*z/v0z)

# print(x(0.014),y(0.014))
def v_y(t):
	return (eta*E(t)/omega)*sin(omega*t)

def v_x(t):
	return (eta*E(t)/omega)*(1-cos(omega*t))	

def v(t):
	return sqrt(v_x(t)**2+v_y(t)**2)

def sina(t):
	return sqrt(v_x(t)**2+v_y(t)**2)/v(t)


print('V_x',v_x(tau))
print('V_y',v_y(tau))
print('B:',B)
print('V_xy(tau):',v(tau))
print('V0z:',v0z)
print('a:',(v(tau)**2)*(1-sqrt(2))/(2*D))
print('R:',v(tau)/(eta*B))

# a=(v(tau)**2)*(1-sqrt(2))/(2*D)
# t=Symbol('t')
# eq=Eq(v0z*t+a/2*t**2,D)
# print(solve(eq))

# def v(z):
# 	return (E/(2*omega))*sqrt(1+2*omega*(sin(omega*z/v0z)-cos(omega*z/v0z))+omega**2)
# print(v(0.016).n(10))
# print(x[-1],y[-1],z[-1])
# ax.plot(x(z),y(z),z, label='parametric', linewidth = 2)


# v0x=1.5
# v0z=1.5
# T=1

# t=np.arange(0,100,0.01)

# omega=(2*pi)/(T)

# x=R*np.sin(t*omega)
# y=R*np.cos(t*omega)-R
# # print(x,y, R, omega)
# # -R/2
# z=v0z*t
# print(x[-1],y[-1],z[-1])
# ax.plot(y, z, -x, label='parametric', alpha=0.3)


# plt.show()

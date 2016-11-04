# -*- coding: UTF-8 -*-

import numpy as np
from scipy.interpolate import UnivariateSpline

from pylab import * 
from math import *
import matplotlib.pyplot as plt

# ex_X- прямое измерение величины X

# def get_A(t):
# 	h=120
# 	return 2*h/t**2

# def get_A_err(t):
#     h=120
#     dH=0.5
#     dT=0.01
#     return (4*t*dH+2*dT*h)/t**3

ex_m1,ex_m2=np.array([
    (0,		48.4),
    (1.48,	46.92),
    (2.6,	45.8),
    (16.6,	31.8),
    (20.1,	28.3)
    ]).T

ex_t1,ex_t2,ex_t3=np.array([
    (2.22, 2.23, 2.21), #последняя точка
    (2.29, 2.31, 2.30),
    (2.36, 2.39, 2.36),
    (4.58, 4.57, 4.6),
    (8.48, 8.1, 8.37) #первая точка
    ]).T

delta_m=ex_m2-ex_m1
t=(ex_t1+ex_t2+ex_t3)/3
a=get_A(t)

# График прямой, полученной методом экстраполяции
x=np.arange(-10,60,0.01)
x=np.arange(0,50,0.01)
func = UnivariateSpline( delta_m, a, k=1 )
y = func(x)
# plot( x, y, "-", color='black')


# График прямой, полученной эмперически
x=np.arange(0,50,0.01)
b=5.70
k=1.123
y=x*k-b

# subplot(1,5,1)
plot( x, y, "-", color='red', linewidth = 0.3)


# subplot(1,5,2)

# xlim(14,16)
# ylim(11,11.8)

dm=0.05
i=0
for counter in delta_m:
    gca().add_patch(Rectangle((delta_m[i]-dm,a[i]-get_A_err(t[i])), 2*dm, 2*get_A_err(t[i]), color="black",fill="black"))
    i+=1

# plot( x, y, "-", color='red', linewidth = 0.3)

# subplot(1,5,3)
# plot( x, y, "-", color='red', linewidth = 0.3)
# subplot(1,5,4)
# plot( x, y, "-", color='red', linewidth = 0.3)


# subplot(1,5,5)
# plot( x, y, "-", color='red', linewidth = 0.3)

# График экспериментальных точек
# plot( delta_m, a, "o", color='blue')print((delta_m[i]-dm)-10*2*dm,a[i]-get_A_err(t[i])-10*2*get_A_err(t[i])

# for TT in t:
#     print(get_A_err(TT))

# dm=0.05

# i=0

# for counter in delta_m:
#     # рассчитываем прямоугольник погрешностей и строим график вокруг него
#     c=5
#     left=((delta_m[i]-dm)-c*2*dm)
#     X=delta_m[i]-dm
#     right=((delta_m[i]-dm)+c*2*dm)
#     arti=get_A_err(t[i])
#     top=(a[i]-arti+c*2*arti)
#     Y=a[i]-arti
#     bottom=(a[i]-arti-c*2*arti)
#     i+=1

#     plt.subplot(1,5,6-i)

#     grid(True)

#     rc('text', usetex=True)
#     rc('font', family='Droid Sans')
#     rc('font', size=11)
#     rc('text.latex',unicode=True)
#     rc('text.latex',preamble=r'\usepackage[utf8]{inputenc}')
#     rc('text.latex',preamble=r'\usepackage[russian]{babel}')  

#     # строим точку на графике
#     # plt.gca().add_patch(Rectangle((delta_m[i]-dm,a[i]-get_A_err(t[i])), 2*dm, 2*get_A_err(t[i]), color="black",fill="black"))   
#     plt.gca().add_patch(Rectangle((X,Y),2*dm,2*arti, color="black",fill="black"))
#     xlim(left,right)
#     ylim(bottom,top)    
#     plt.plot( x, y, "-", color='red', linewidth = 0.3)
#     pass


# # Вывод графика
# # tight_layout()


grid(True)

axhline(y=0, color='black')
axvline(x=0, color='black')

rc('text', usetex=True)
rc('font', family='Droid Sans')
rc('text.latex',unicode=True)
rc('text.latex',preamble=r'\usepackage[utf8]{inputenc}')
rc('text.latex',preamble=r'\usepackage[russian]{babel}')

xlabel(r'$\Delta{m}$')
ylabel(r'a($\Delta{m}$)')

# title(r'График зависимости ускорения грузов от изменения $m_2-m_1$')
ylim(-8,53)
xlim(0,50)

# # savefig( "img/ex_22.png", dpi=300 )
# # show()
# # 
# M=363
# mass=48.4
# g=981

# gamma=g/k-(2*M+mass)
# F0=b*(2*M+mass+gamma)

# print(gamma, F0)

# def a2(dM):
# 	return (dM*g-F0)/(2*M+mass+gamma)

# # print(a2(delta_m))
# # print(np.round(a,4))

# print(F0/g)
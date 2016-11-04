# -*- coding: UTF-8 -*-

import numpy as np
from scipy.interpolate import UnivariateSpline

from pylab import * 
from math import *
import matplotlib.pyplot as plt

# ex_X- прямое измерение величины X

def get_A(t):
	h=120
	return 2*h/t**2

def get_A_err(t):
    h=120
    dH=0.5
    dT=0.01
    return (4*t*dH+2*dT*h)/t**3


def get_A_er_arr(T):
    tt=[]
    for t in T:
        h=120
        dH=0.5
        dT=0.01
        tt.append((4*t*dH+2*dT*h)/t**3)
    return tt

def get_T_er_arr(T):
    tt=[]
    for t in T:
        dT=0.01
        tt.append(2*dT*t)
    return tt

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

m_=delta_m.mean()
a_=a.mean()



print('---',m_,a_)

R_ma=0
i=0
for xxx in delta_m:
    R_ma+=(delta_m[i]-m_)*a[i]
    i+=1
R_ma=R_ma/i

S_kv=0
i=0
for xxx in delta_m:
    S_kv+=(delta_m[i]-m_)**2
    i+=1
dm_kv=S_kv
S_kv=S_kv/i  

print(R_ma,S_kv,R_ma/S_kv)  
k=R_ma/S_kv
print(a_-R_ma/S_kv*m_)
b=a_-R_ma/S_kv*m_

test=0
i=0
for xxx in delta_m:
    test+=(a[i]-b-k*delta_m[i])**2
    i+=1
d_kv=math.sqrt(test/3)

a_kv=0
i=0
for xxx in delta_m:
    a_kv+=(a[i]-a_)**2
    i+=1

# print('r/b:',dm_kv/a_kv)

M=363
dM=0.5
mass=48.4
eK=0.0097
Lambda=99.15
dF=164.8131
F=4979.25
g=981

# (m_2-m_1)g-a(2M+m_1+m_2+\lambda)
print('=========')
i=0
for temp in delta_m:
    print('F_0=',delta_m[i]*g-a[i]*(2*M+mass+Lambda))
    i+=1
print('=========')
dLambda=eK*(2*M+mass+Lambda)-4*dM
# print(dLambda)
print(Lambda-dLambda,Lambda,Lambda+dLambda)


print((F-dF),(F+dF))



# \sqrt{\frac{0.015246}{3}} 

# print('---')
# print('m1',np.round(ex_m1,2))
# print('m2',np.round(ex_m2,2))
# print('Delta m',np.round(delta_m,2))
# print('---')
# print('t1',np.round(ex_t1,2))
# print('t2',np.round(ex_t1,2))
# print('t3',np.round(ex_t1,2))
# print('t',np.round(t,2))
# print('t^2',np.round(t**2,2))
# print('---ERR-t^2',np.round(get_A_er_arr(t**2),4))
# print('---')
# print('a=2h/(t^2)',np.round(a,2))
# print('---ERR-a',np.round(get_A_er_arr(a),4))
# print('---')

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
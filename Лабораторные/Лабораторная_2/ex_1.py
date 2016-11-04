# -*- coding: UTF-8 -*-

import numpy as np
from scipy.interpolate import UnivariateSpline

from pylab import * 
from math import *

# ex_X- прямое измерение величины X

# def get_A(t):
# 	h=120
# 	return 2*h/t**2

# def get_A_err(t):
#     h=120
#     dH=0.5
#     dT=0.01
#     return (2*t*dH+dT*h)/t**3

grid(c='#cccccc',ls='-')

axhline(y=0, color='black')
axvline(x=0, color='black')
ylim(0,25)
rc('text', usetex=True)
rc('font', family='Droid Sans')
rc('font', size=15)
rc('text.latex',unicode=True)
rc('text.latex',preamble=r'\usepackage[utf8]{inputenc}')
rc('text.latex',preamble=r'\usepackage[russian]{babel}')

xlabel(r'$h(t^2)$, см')
ylabel(r'$t^2$, $c^2$')

labels=[]
for x in range(0,101):
    labels.append('')
# labels[0]='0'
x=np.arange(0,101)
a=[0,10,40,50,80,90,100]

# c=0
for A in a:
    # print(A,c)
    # if c==A:
    print(A)
    labels[A]=str(A)
    # c+=1

# xticks(x, labels, rotation='vertical')

ylabels=[]
for y in range(0,26):
    ylabels.append('')
# labels[0]='0'
y=np.arange(0,26)
y=[0,5,10,15,20,25]
for A in y:
    print(A)
    ylabels[A]=str(A)

def get_tt_err(t):
    dT=0.01
    return (2*t*dT)

m1_t1,m1_t2,m1_t3=np.array([
    (1.72,  1.80,   1.76),
    (1.98,  1.95,   1.96),
    (2.48,  2.50,   2.51),
    (2.66,  2.65,   2.64),
    (2.79,  2.81,   2.80)
   ]).T

m2_t1,m2_t2,m2_t3=np.array([
    (2.81,  2.83,   2.85),
    (3.19,  3.18,   3.22),
    (4.03,  4.01,   3.98),
    (4.26,  4.23,   4.24),
    (4.49,  4.42,   4.50)
    ]).T

m3_t1,m3_t2,m3_t3=np.array([
    (1.26,  1.32,   1.31),
    (1.43,  1.45,   1.48),
    (1.87,  1.90,   1.88),
    (1.97,   2.00,   1.95),
    (2.08,  2.06,   2.09)
    ]).T

h=np.array([40,50,80,90,100])

m1_tkv=((m1_t1+m1_t2+m1_t3)/3)**2
# print((m1_t1+m1_t2+m1_t3)/3)
m2_tkv=((m2_t1+m2_t2+m2_t3)/3)**2
# print((m2_t1+m2_t2+m2_t3)/3)
m3_tkv=((m3_t1+m3_t2+m3_t3)/3)**2
# print((m3_t1+m3_t2+m3_t3)/3)
# a=get_A(t)

# График прямой, полученной методом экстраполяции
# x=np.arange(-10,60,0.01)

x=np.arange(0,100,0.1)
func = UnivariateSpline( h, m1_tkv, k=1 )
y = func(x)
plot( x, y, "-", color='black', linewidth = 0.7)


# x=np.arange(0,100,0.1)
func = UnivariateSpline( h, m2_tkv, k=1 )
y = func(x)
plot( x, y, "-", color='red', linewidth = 0.7)

# x=np.arange(0,100,0.1), linewidth = 0.5
func = UnivariateSpline( h, m3_tkv, k=1 )
y = func(x)
plot( x, y, "-", color='green', linewidth = 0.7)

# График прямой, полученной эмперически
# x=np.arange(0,50,0.01)
# b=5.70
# k=1.123
# y=x*k-b
# ylim(-8,53)

# plot( x, y, "-", color='red', linewidth = 0.3)


# График экспериментальных точек
# plot( h, m1_tkv, marker = 's', linestyle = '', color='black', label='m=28.3 грамм')
# plot( h, m2_tkv, marker = 's', linestyle = '', color='red', label='m=14 грамм')
# plot( h, m3_tkv, marker = 's', linestyle = '', color='green',label='m=42.3 грамм')

legend(loc = 2)

# yticks(y, ylabels)
# for TT in t:
#     print(get_A_err(TT))

# m1_tkv ---t
def kvadrat_err(txt,arr,color):
    dh=0.5
    i=0
    for counter in h:
        gca().add_patch(Rectangle((h[i]-dh,arr[i]-get_tt_err(arr[i])), 2*dh, 2*get_tt_err(arr[i]), color="black"))
        print(txt,': h=',h[i],' t^2=',arr[i],' dH=0.5 ','d(t^2)=',get_tt_err(arr[i]))
        print('')
        i+=1

kvadrat_err('m1=28.3 грамм',m1_tkv,"black")
kvadrat_err('m2=14 грамм',m2_tkv,"red")
kvadrat_err('m3=42.3 грамм',m3_tkv,"green")
# Вывод графика

# title(r'График зависимости пройденного пути от квадрата времени')

def get_T_er_arr(T):
    tt=[]
    for t in T:
        dT=0.01
        tt.append(2*dT*t)
    return tt

# savefig( "img/ex1.eps")#, dpi=300 )
# show()
# print('m1=28.3, m2=14, m3=42.3')
# print('h',h)
# print('---')
# print('m1-t1',np.round(m1_t1,2))
# print('m1-t2',np.round(m1_t2,2))
# print('m1-t3',np.round(m1_t3,2))
# print('m1-t',np.round(np.sqrt(m1_tkv),2))
# print('m1-t^2',np.round(m1_tkv,2))
# print('---ERR-t^2',np.round(get_T_er_arr(m1_tkv),4))
# print('---')
# print('m2-t1',np.round(m2_t1,2))
# print('m2-t2',np.round(m2_t2,2))
# print('m2-t3',np.round(m2_t3,2))
# print('m2-t',np.round(np.sqrt(m2_tkv),2))
# print('m2-t^2',np.round(m2_tkv,2))
# print('---ERR-t^2',np.round(get_T_er_arr(m2_tkv),4))
# print('---')
# print('m3-t1',np.round(m3_t1,2))
# print('m3-t2',np.round(m3_t2,2))
# print('m3-t3',np.round(m3_t3,2))
# print('m3-t',np.round(np.sqrt(m3_tkv),2))
# print('m3-t^2',np.round(m3_tkv,2))
# print('---ERR-t^2',np.round(get_T_er_arr(m3_tkv),4))
# print('---')









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
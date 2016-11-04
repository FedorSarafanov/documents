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

m1_t1,m1_t2,m1_t3=np.array([
    (1.72,  1.80,   1.76),
    (1.98,  1.95,   1.96),
    (2.08,  2.45,   2.55),
    (2.66,  2.54,   2.60),
    (2.72,  2.75,   2.90)
   ]).T

m2_t1,m2_t2,m2_t3=np.array([
    (2.81,  2.83,   2.85),
    (3.19,  3.18,   3.22),
    (3.98,  4.01,   3.98),
    (4.20,  4.23,   4.24),
    (4.55,  4.42,   4.50)
    ]).T

m3_t1,m3_t2,m3_t3=np.array([
    (1.26,  1.32,   1.31),
    (1.43,  1.45,   1.48),
    (1.87,  1.90,   1.88),
    (1.97,   2.00,   1.95),
    (2.02,  2.03,   2.02)
    ]).T

h=np.array([40,50,80,90,100])

m1_tkv=((m1_t1+m1_t2+m1_t3)/3)**2
print((m1_t1+m1_t2+m1_t3)/3)
m2_tkv=((m2_t1+m2_t2+m2_t3)/3)**2
print((m2_t1+m2_t2+m2_t3)/3)
m3_tkv=((m3_t1+m3_t2+m3_t3)/3)**2
print((m3_t1+m3_t2+m3_t3)/3)
# a=get_A(t)

# График прямой, полученной методом экстраполяции
# x=np.arange(-10,60,0.01)

x=np.arange(0,100,0.1)
func = UnivariateSpline( h, m1_tkv, k=1 )
y = func(x)
plot( x, y, "-", color='black')


# x=np.arange(0,100,0.1)
func = UnivariateSpline( h, m2_tkv, k=1 )
y = func(x)
plot( x, y, "-", color='red')

# x=np.arange(0,100,0.1)
func = UnivariateSpline( h, m3_tkv, k=1 )
y = func(x)
plot( x, y, "-", color='green')

# График прямой, полученной эмперически
# x=np.arange(0,50,0.01)
# b=5.70
# k=1.123
# y=x*k-b
# ylim(-8,53)
# xlim(0,50)
# plot( x, y, "-", color='red', linewidth = 0.3)


# График экспериментальных точек
plot( h, m1_tkv, marker = 's', linestyle = '--', color='black', label='m=28.3 грамм')
plot( h, m2_tkv, marker = 's', linestyle = '--', color='red', label='m=14 грамм')
plot( h, m3_tkv, marker = 's', linestyle = '--', color='green',label='m=42.3 грамм')

legend(loc = 2)
xticks([0,10,40,50,80,90,100])
# for TT in t:
#     print(get_A_err(TT))

# dm=0.05
# i=0
# for counter in delta_m:
#     gca().add_patch(Rectangle((delta_m[i]-dm,a[i]-get_A_err(t[i])), 2*dm, 2*get_A_err(t[i]), color="black",fill="black"))
#     i+=1


# Вывод графика

grid(True)

axhline(y=0, color='black')
axvline(x=0, color='black')

rc('text', usetex=True)
rc('font', family='Droid Sans')
rc('font', size=15)
rc('text.latex',unicode=True)
rc('text.latex',preamble=r'\usepackage[utf8]{inputenc}')
rc('text.latex',preamble=r'\usepackage[russian]{babel}')

xlabel(r'$h(t^2)$, см')
ylabel(r'$t^2$, $c^2$')

# title(r'График зависимости пройденного пути от квадрата времени')

savefig( "img/ex1.png", dpi=300 )
show()

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
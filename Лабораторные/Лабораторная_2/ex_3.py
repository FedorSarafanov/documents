# -*- coding: UTF-8 -*-

import numpy as np
from scipy.interpolate import UnivariateSpline

from pylab import * 
from math import *

# ex_X- прямое измерение величины X

# def get_A(t):
#   h=120
#   return 2*h/t**2

# def get_A_err(t):
#     h=120
#     dH=0.5
#     dT=0.01
#     return (2*t*dH+dT*h)/t**3

m1_t1,m1_t2,m1_t3=np.array([
    (3.16,  3.20,   3.22),
    (3.49,  3.52,   3.48),
    (3.78,  3.80,   3.81),
    (4.12,  4.10,   4.11),
    (4.41,  4.42,   4.41)
   ]).T

m2_t1,m2_t2,m2_t3=np.array([
    (2.30,  2.29,   2.28),
    (2.48,  2.51,   2.54),
    (2.71,  2.74,   2.72),
    (2.97,  3.00,   2.99),
    (3.20,  3.20,   3.23)
    ]).T

m3_t1,m3_t2,m3_t3=np.array([
    (3.09,  3.10,   3.10),
    (3.38,  3.45,   3.42),
    (3.72,  3.75,   3.75),
    (4.06,  4.12,   4.08),
    (4.41,  4.39,   4.40)
    ]).T

h=np.array([50,60,70,80,90])

m1_tkv=((m1_t1+m1_t2+m1_t3)/3)
# print((m1_t1+m1_t2+m1_t3)/3)
m2_tkv=((m2_t1+m2_t2+m2_t3)/3)
# print((m2_t1+m2_t2+m2_t3)/3)
m3_tkv=((m3_t1+m3_t2+m3_t3)/3)
# print((m3_t1+m3_t2+m3_t3)/3)
# a=get_A(t)

m1_t0=(1.5+1.48+1.51)/3
m2_t0=(1.09+1.09+1.09)/3
m3_t0=(1.53+1.49+1.48)/3

m1_tkv=m1_tkv-m1_t0
# print(m1_tkv)
m2_tkv=m2_tkv-m2_t0
# print(m2_tkv)
m3_tkv=m3_tkv-m3_t0
# print(m3_tkv)
dm1=m2_tkv[0]-m1_tkv[0]
dm2=m3_tkv[0]-m1_tkv[0]
m2_tkv=m1_tkv+dm1
m3_tkv=m1_tkv+dm2

def kvadrat_err(txt,arr):
    dh=0.5
    dt=0.01
    i=0
    for counter in h:
        gca().add_patch(Rectangle((h[i]-dh,arr[i]-dt), 2*dh, 2*dt, color="black"))
        print(h[i]-dh,arr[i]-dt)
        print(txt,': h=',h[i],' t=',arr[i],' dH=0.5 ','dt=0.01')
        print('')
        i+=1

kvadrat_err('m1',m1_tkv)
kvadrat_err('m2',m2_tkv)
kvadrat_err('m3',m3_tkv)
# print(m1_tkv)

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
ylim(1,3.5)
xlim(45,95)
# plot( x, y, "-", color='red', linewidth = 0.3)


# График экспериментальных точек
# print(h)
# plot( h, m1_tkv, marker = 's', linestyle = '--', color='black', label='m=15.7 грамм')
# plot( h, m3_tkv, marker = 's', linestyle = '--', color='green',label='m=15.8 грамм')
# plot( h, m2_tkv, marker = 's', linestyle = '--', color='red', label='m=23.7 грамм')


legend(loc = 2)
# xticks([0,10,40,50,80,90,100])
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

xlabel(r'$h(t)$, см')
ylabel(r'$t$, $c$')

def get_T_er_arr(T):
    tt=[]
    for t in T:
        dT=0.01
        tt.append(2*dT*t)
    return tt

savefig( "img/ex4.png", dpi=300 )
# savefig( "img/ex4.png")
# show()/
# print('m1=15.7, m2=23.7, m3=15.8')
# print('h',h)
# print('---')
# print('m1-t1',np.round(m1_t1,2))
# print('m1-t2',np.round(m1_t2,2))
# print('m1-t3',np.round(m1_t3,2))
# print('m1-t',np.round((m1_tkv),2))
# # print('---ERR-t^2',np.round(get_T_er_arr(m1_tkv),4))
# print('---')
# print('m2-t1',np.round(m2_t1,2))
# print('m2-t2',np.round(m2_t2,2))
# print('m2-t3',np.round(m2_t3,2))
# print('m2-t',np.round((m2_tkv),2))
# # print('---ERR-t^2',np.round(get_T_er_arr(m2_tkv),4))
# print('---')
# print('m3-t1',np.round(m3_t1,2))
# print('m3-t2',np.round(m3_t2,2))
# print('m3-t3',np.round(m3_t3,2))
# print('m3-t',np.round((m3_tkv),2))
# # print('---ERR-t^2',np.round(get_T_er_arr(m3_tkv),4))
# print('---')
# print('m1-t0',np.round(m1_t0,2))
# print('m2-t0',np.round(m2_t0,2))
# print('m3-t0',np.round(m3_t0,2))


# savefig( "img/ex4.eps")
# show()


# # -*- coding: utf-8 -*-
import math, random
from math import *
# pi=3.1415926
# l=95.
# g=981.
# T1=[0,0,0]
# T2=[0,0,0]
# dH=[92,112,122]
# dN=[20,25,30]

# def G(dL,N,t2,t1):
# 	return 4*(pi**2)*dL*(N**2)/(t2**2-t1**2)/100

# N=20
# # for l in [95,115,125]: 	
# 	# print(round(N*(2*pi*math.sqrt(l/(g+g/100))),2),',',round(N*(2*pi*math.sqrt(l/(g-g/100))),2))

# # g=4*(pi**2)*l/N**2

# T2[0]=20*(2*pi*math.sqrt(95/g))
# T2[1]=25*(2*pi*math.sqrt(115/g))
# T2[2]=30*(2*pi*math.sqrt(125/g))

# l1=3.; l2=95.; t1=31.2; t2=49.6; N=20.;
# # print(G(l2-l1,N,t2,t1)*100)
# # if G(l2-l1,N,t2,t1)*100<=g+g/100:
# # 	if G(l2-l1,N,t2,t1)*100>=g-g/100:
# # 		print ('t1:',t1/N)
# # 		print ('H2:',l2)
# # 		print ('t2:',t2)
# # 		print ('T2:',t2/N)
# # 		print ('h2-h1:',l2-l1)
# # 		print ('T2^2-T1^2:',(t2/N)**2-(t1/N)**2)
# # 		print ('g:',G(l2-l1,N,t2,t1)*100)

# print((987.742+977.667+986.415)/3)
# print(g+g/100)
# print(g-g/100)


# n=[20,25,30]
# # n=[20,20,20]
# h1=[3,3,3]
# t1=[[6.91,6.98],[8.64,8.73],[10.37,10.48]]
# h2=[95,115,125]
# t2=[[38.91,39.3],[53.51,54.05],[66.95,67.62]]
# # t2=[[38.91,39.3],[42.81 , 43.24],[44.63,45.08]]
# for x in [0,1,2]:
# 	tt1=random.uniform(t1[x][0],t1[x][1])
# 	tt2=random.uniform(t2[x][0],t2[x][1])
# 	print('h1:',h1[x])
# 	print('t1:',round(tt1,2))
# 	print('T1:',round(tt1/n[x],2))
# 	print('h2:',h2[x])
# 	print('t2:',round(tt2,2))
# 	print('T2:',round(tt2/n[x],2))
# 	print('h2-h1:',h2[x]-h1[x])
# 	print('T2^2-T1^2',round((tt2/n[x])**2-(tt1/n[x])**2,3))
# 	print('Расчетное G:',G(h2[x]-h1[x],n[x],tt2,tt1)*100)
# 	if G(h2[x]-h1[x],n[x],tt2,tt1)*100<=g+g/100:
# 		if G(h2[x]-h1[x],n[x],tt2,tt1)*100>=g-g/100:
# 			print('G подходит')
# 	print('---------------------')

# 	pass

dT=0.2
dh=0.1

# def y(T2,T1,h2,h1):
# 	return (2*dT)/((T2-T1)*(0.01-(2*dh)/(h2-h1)))

# def my(T2,T1,h2,h1):
# 	return (math.sqrt(T2**2-T1**2)*(0.01-sqrt(2)*dh/(h2-h1)))/(2*dT)

# print(y(4.999,2,45,20), my(4,2,40,20))

# T2=1.96
# T1=0.35
# h2=95
# h1=3
# n=25
# print(2*dT/(n*(T2-T1))+2*dh/(h2-h1))
# print((0.014*987.74+0.012*977.66+0.01*986.41)/(987.74+977.66+986.41))
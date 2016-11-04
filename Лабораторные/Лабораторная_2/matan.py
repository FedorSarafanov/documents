from math import *

# print(sqrt(5/0.09-2/3))

g=981
M=363

dM=0.5
dm=0.05
dH=0.5
dT=0.01

k=1.146
b=7.62

delta=48.4
mass=48.4

# k=g/(2*m+mass+gamma)
a=49.6
gamma=(g/k-((2*M+mass)))
F0=(2*M+mass+gamma)*b

print("gamma =",gamma)

ro=2.69
R=3.588
d=1.5
pi=3.14
r=0.3



V=pi*(R**2)*d

I=V*ro*R**2/2

print("I/R^2 =",I/R**2)

print("F0 =",(2*M+mass+gamma)*b,"дин =",(2*M+mass+gamma)*b/10**5,"Н")

print("eq: ",F0*r+gamma*a*R,"=?=",I*a/R)

# print((3.47+7.62)/9.68)

dT=0.2
dH=0.1

def n(T1,T2,H1,H2):
	return 2*dT/((T2-T1)*(0.01-2*dH/(H2-H1)))

T1=[0.35,0.44,0.52]
T2=[1.96,2.15,2.25]
H1=[3,3,3]
H2=[95,115,125]

c=0
for x in T1:
	print(n(T1[c],T2[c],H1[c],H2[c]))
	c+=1
	pass

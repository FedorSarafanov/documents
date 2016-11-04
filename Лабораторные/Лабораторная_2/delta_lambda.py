R1=9
R2=8.7
d1=0.5
d2=0.02

Lambda=100.74
def function(R1,R2,d1,d2):
	dx=0.01
	return 2*dx*(2*(R2**3)*(d2**2)/(R1**2)+
		(R2**4)*d2/(R1**2)+
		(R2**4)*(d2**2)/(R1**3)+
		(d1**2)*R1+
		(R1**2)*d1)
dl=function(R1,R2,d1,d2)
print(Lambda-dl,Lambda,Lambda+dl)


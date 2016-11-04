# -*- coding: UTF-8 -*-

import numpy as np
from scipy.interpolate import UnivariateSpline
    # pydoc scipy.interpolate.UnivariateSpline -- fitpack, unclear
from datetime import date
from pylab import *  # ipython -pylab

# from matplotlib import rc


from math import *

# -7.62

__version__ = ""

g=9.81
M=363
dM=0.5
dm=0.05

k=11.44/16.68

dH=0.5
dT=0.01

def errA(H,T):
    dH=0.5
    dT=0.01

    a=(2*H/T**2)
    print(a)
    dA=dH/H-(2*dT)/T
    return abs(dA*a)

dA=49.6*(dH/120-2*(dT/2.2))

print(errA(120,2.2))
print(dA)
print('---')

deltaM,a=np.array([
    (48.4,49.6),#!47.64
    # (48.4,47.69),
    (45.44,44.3),
    (44.68,42.40),#!43.76
    # (44.68,43.76),
    (16.68,11.44),
    (9.68,3.47)
    ]).T


approx=np.array([-5,0,5,10,15,20,25,30,35,40,45,50,55,60])

approx=np.arange(-5,60,0.01)

x2=np.arange(-5,60,0.01)
y2=x2*1.14-7.62

extrapolatorer = UnivariateSpline( deltaM, a, k=1 )
z = extrapolatorer( approx )


# i=0
# for counter in deltaM:
#     gca().add_patch(Rectangle((deltaM[i]-dm,a[i]-dA/2), dA, 2*dm, fill="red"))
#     i+=1

plot( approx, z, "-" )
# plot( x2, y2, "-", color='red')




plot( deltaM, a, "o",color='black' )

plot( 0, -7.62, "o",color='blue' )

# def daynumber( y,m,d ):
#     """ 2005,1,1 -> 0  2006,1,1 -> 365 ... """
#     return date( y,m,d ).toordinal() - date( 2005,1,1 ).toordinal()

# days, values = np.array([
#     (daynumber(2005,1,1), 1.2 ),
#     (daynumber(2005,4,1), 1.8 ),
#     (daynumber(2005,9,1), 5.3 ),
#     (daynumber(2005,10,1), 5.3 )
#     ]).T
# dayswanted = np.array([ daynumber( year, month, 1 )
#         for year in range( 2005, 2006+1 )
#         for month in range( 1, 12+1 )])

# np.set_printoptions( 1 )  # .1f
# print "days:", days
# print "values:", values
# print "dayswanted:", dayswanted


# plot( days, values, "o" )
# for k in (1,2,3):  # line parabola cubicspline
#     extrapolator = UnivariateSpline( days, values, k=k )
#     y = extrapolator( dayswanted )
#     label = "k=%d" % k
#     print label, y
#     plot( dayswanted, y, label=label  )  # pylab

# legend( loc="lower left" )
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
title(r'График зависимости ускорения грузов от изменения $m_2-m_1$')
# legend(loc = 'best')

savefig( "график.png", dpi=300 )
show()


print(dA)

m_1=0
m_2=48.4

gamma=g/k-(2*M+m_1+m_2)

F0=7.62*(2*M+m_1+m_2+gamma)

print("AAA",gamma, F0)
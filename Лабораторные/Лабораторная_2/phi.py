# -*- coding: UTF-8 -*-

import numpy as np
from scipy.interpolate import UnivariateSpline

from pylab import * 
from math import *

# ex_X- прямое измерение величины X

x=np.arange(0,0.3,0.01)
y=np.sin(x)

# plot( x, y, "-", color='blue')
# plot( x, x, "-", color='red')
# plot (0.2 , sin(0.2),"o")
# print(0.2*57.3)

# Вывод графика

T=[8.6,4.3,2.97,2.19,2.4]
phi=[5,10,15,20,40]

x=np.arange(0,40,0.01)
# func = UnivariateSpline( T, phi, k=3 )
# y = func(x)
# plot( x, y, "-", color='black')



i=0
for counter in T:
    gca().add_patch(Rectangle((phi[i]-0.5,T[i]-0.2), 1, 0.4, color="black"))
    i+=1

plot( phi, T, "o", color='white')
grid(True)

axhline(y=0, color='black')
axvline(x=0, color='black')

rc('text', usetex=True)
rc('font', family='Droid Sans')
rc('font', size=15)
rc('text.latex',unicode=True)
rc('text.latex',preamble=r'\usepackage[utf8]{inputenc}')
rc('text.latex',preamble=r'\usepackage[russian]{babel}')

xlabel(r'$\phi$, градусы')
ylabel(r'T($\phi$), секунды')

# title(r'\vspace{5mm}')

savefig( "phi_2.png", dpi=300 )
# savefig( "sin.png", dpi=300 )
show()
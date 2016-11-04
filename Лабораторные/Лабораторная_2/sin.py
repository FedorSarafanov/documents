# -*- coding: UTF-8 -*-

import numpy as np
from scipy.interpolate import UnivariateSpline

from pylab import * 
from math import *

# ex_X- прямое измерение величины X

x=np.arange(0,0.3,0.01)
y=np.sin(x)

plot( x, y, "-", color='blue')
plot( x, x, "-", color='red')
plot (0.2 , sin(0.2),"o")
print(0.2*57.3)

# Вывод графика

T=[8.6,4.3,2.97,2.19,2.4]
phi=[5,10,15,20]

grid(True)

axhline(y=0, color='black')
axvline(x=0, color='black')

rc('text', usetex=True)
rc('font', family='Droid Sans')
rc('text.latex',unicode=True)
rc('text.latex',preamble=r'\usepackage[utf8]{inputenc}')
rc('text.latex',preamble=r'\usepackage[russian]{babel}')

xlabel(r'$sin(\phi)$')
ylabel(r'Угол $\phi$, радиан')

title(r'График зависимости $sin(\phi)$ от $\phi$. Верхняя линия --- $y=x$, нижняя --- $y=sin(x)$')

savefig( "sin.png", dpi=300 )
show()
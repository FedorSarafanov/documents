import latable as lt
import numpy as np

import re

from scipy.interpolate import UnivariateSpline

from pylab import * 
from math import *

def table(columns,rows,errors, mcol):

	# columns = '|c|c|c|c|c|'
	header = r'\begin{tabular}{' + columns + r'}'
	# Find the number of columns. Note that this does *not* handle *{}{}!
	numcols = len(re.findall('l|c|r|p{.*?}', columns))
	# rows = []
	footer = r'\end{tabular}'

	table = [header]
	table += ['\hline']

	# a = np.array(h, dtype='<U4')
	# a = a.astype(np.str)	
	i=0
	for ARROW in rows:
		row=[]
		for txt in ARROW:
			if mcol!=0:
				text=r'\multicolumn{'+str(mcol)+r'}{|c|}{'+str(txt)+errors[i]+'}'
			else:
				text=str(txt)+errors[i]
			row.append(text)
		table += [' & '.join(row)+r'\\']
		table += [r'\hline']
		i+=1


	table += [footer]
	return '\n'.join(table)

def row(rows,errors, mcol):

	table = []

	i=0
	for ARROW in rows:
		row=[]
		for txt in ARROW:
			if mcol!=0:
				text=r'\multicolumn{'+str(mcol)+r'}{|c|}{'+str(txt)+errors[i]+'}'
			else:
				text=str(txt)+errors[i]
			row.append(text)
		table += [' & '.join(row)+r'\\']
		table += [r'\hline']
		i+=1
	return '\n'.join(table)

m1_T=np.array([
    (1.72,  1.80,   1.76),
    (1.98,  1.95,   1.96),
    (2.08,  2.45,   2.55),
    (2.66,  2.54,   2.60),
    (2.72,  2.75,   2.90)
   ])

m1_t1,m1_t2,m1_t3=m1_T.T

m1_t123=[item for sublist in m1_T.tolist() for item in sublist]
# print(m1_t123)

m2_T=np.array([
    (2.81,  2.83,   2.85),
    (3.19,  3.18,   3.22),
    (3.98,  4.01,   3.98),
    (4.20,  4.23,   4.24),
    (4.55,  4.42,   4.50)
    ])

m2_t1,m2_t2,m2_t3=m2_T.T

m2_t123=[item for sublist in m2_T.tolist() for item in sublist]
# print(m2_t123)


m3_T=np.array([
    (1.26,  1.32,   1.31),
    (1.43,  1.45,   1.48),
    (1.87,  1.90,   1.88),
    (1.97,   2.00,   1.95),
    (2.02,  2.03,   2.02)
    ])

m3_t1,m3_t2,m3_t3=m3_T.T

m3_t123=[item for sublist in m3_T.tolist() for item in sublist]
# print(m3_t123)

h=np.array([40,50,80,90,100])

m1_t=((m1_t1+m1_t2+m1_t3)/3)
m2_t=((m2_t1+m2_t2+m2_t3)/3)
m3_t=((m3_t1+m3_t2+m3_t3)/3)

m1_tkv=((m1_t1+m1_t2+m1_t3)/3)**2
m2_tkv=((m2_t1+m2_t2+m2_t3)/3)**2
m3_tkv=((m3_t1+m3_t2+m3_t3)/3)**2

# print(table('|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|',[h.tolist()],[r' $\pm 0.5 \text{см}$',r' $\pm 0.01 c$'],3))

print(row([m1_t123],[r' $\pm 0.5 \text{см}$',r' $\pm 0.01 c$'],0))

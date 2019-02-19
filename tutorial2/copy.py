"""
Carlos Mateos 
s2076861
intro test
"""

import numpy as np

# 1a 
vector=np.arange(1,101)
vector_average=np.average(vector)
vector_stand_deviation=np.std(vector)

#1b
vector_even=[]
for i in range(len(vector)):
    if i%2==0:
        vector_even.append(i)

vector_average_even=np.average(vector_even)
vector_stand_deviation_even=np.std(vector_even)

vector_odd=[]
for i in range(len(vector)):
    if i%2!=0:
        vector_odd.append(i)

vector_average_odd=np.average(vector_odd)
vector_stand_deviation_odd=np.std(vector_odd)

#1 c and d
vector_inside=[]
vector_outside=[]
for i in range(len(vector)):
    if i in  np.arange(10,21) or i in np.arange(45,58): 
        vector_outside.append(i)
    else:
        vector_inside.append(i)

vector_average_c=np.average(vector_inside)
vector_stand_deviation_c=np.std(vector_inside)

vector_average_d=np.average(vector_outside)
vector_stand_deviation_d=np.std(vector_outside)


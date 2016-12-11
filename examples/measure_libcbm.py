import sys

# add a directory to the module search paths for pycbm
sys.path.append("../module")

import pycbm
import array
import random
import numpy as np
import time
from matplotlib import pyplot as plt

N = 1024         # max buffer size
M = 4294967295   # single value range (U32)
R = 100          # averaging rounds

popcnt_buff_in  = array.array('I', range(N))
popcnt_buff_out = array.array('I', range(N))

bitrev_buff_in  = array.array('I', range(N))
bitrev_buff_out = array.array('I', range(N))

# populate buffers with randome values
for i in range(N):
	popcnt_buff_in[i] = random.randint(0,M)
	bitrev_buff_in[i] = random.randint(0,M)

lib = pycbm.pycbm();

popcnt_y_data = []
bitrev_y_data = []
x_data = []

for i in range(N):
	t0 = time.time()
	for r in range(R):
		lib.popcnt32n(popcnt_buff_in[0:i+1], popcnt_buff_out[0:i+1])
	t1 = time.time()
	for r in range(R):
		lib.bitrev32n(bitrev_buff_in[0:i+1], bitrev_buff_out[0:i+1])
	t2 = time.time()
	
	avg_popcnt32n_time = (t1-t0)/R
	avg_bitrev32n_time = (t2-t1)/R
	
	x_data.append(i+1)
	popcnt_y_data.append(avg_popcnt32n_time)
	bitrev_y_data.append(avg_bitrev32n_time)
	
print(len(x_data),len(popcnt_y_data), len(bitrev_y_data))
	
fig, tgraph = plt.subplots()
tgraph.plot(np.array(x_data),np.array(popcnt_y_data), label='popcnt32n')
tgraph.plot(np.array(x_data),np.array(bitrev_y_data), label='bitrev32n')
legend = tgraph.legend(loc='upper center', shadow=True)
plt.show()

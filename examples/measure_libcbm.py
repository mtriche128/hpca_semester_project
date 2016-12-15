################################################################################
# File  : measure_libcbm.py                                                    #
# Brief : This experiment measures the performance of functions within libcbm. #
# Author: Matthew Triche                                                       #
#                                                                              #                                                       
# Permission is hereby granted, free of charge, to any person obtaining a copy #
# of this software and associated documentation files (the "Software"), to     #
# deal in the Software without restriction, including without limitation the   #
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or  #
# sell copies of the Software, and to permit persons to whom the Software is   #
# furnished to do so, subject to the following conditions:                     #
#                                                                              #
# The above permission notice shall be included in all copies or substantial   #
# portions of the Software.                                                    #
#                                                                              #
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR   #
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,     #
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  #
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER       #
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING      #
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS #
# IN THE SOFTWARE.                                                             #
################################################################################

import sys

# add a directory to the module search paths for pycbm
sys.path.append("../module")

import threading
import pycbm
import array
import random
import numpy as np
import time
from matplotlib import pyplot as plt

################################################################################
# Define Constants                                                             #
################################################################################

M = 4294967295   # single value range (U32)

################################################################################
# Define Classes                                                               #
################################################################################

# ------------------------------------------------------------------------------
# BenchmarkJob
#
# This class is used to encapsulate the function pointer and work buffers used
# to execute a given benchmarking job.

class BenchmarkJob:
	# ------------------------------------------------------------------------
	# __init__
	#
	# This constructor creates the work buffers used by the assigned function.
	#
	# Arguments:
	# func - The assigned function pointer.
	# size - The work buffer size.
	
	def __init__(self, func, size):
		self.func     = func
		self.buff_in  = array.array('I', range(size))
		self.buff_out = array.array('I', range(size))
		
		# populate buffers with randome values
		for i in range(size):
			self.buff_in[i]  = random.randint(0,M)
			self.buff_out[i] = random.randint(0,M)
			
	# ------------------------------------------------------------------------------
	# execute
	#
	# Execute the benchmark job.
	#
	# Arguments:
	# size  - Work buffer size used.
	# it    - The number of iterations executed.
	# accum - The thread-safe accumulator.

	def execute(self,size,it,accum):
		t0 = time.time()
		for i in range(it):
			self.func(self.buff_in[0:size], self.buff_out[0:size])
		t1 = time.time()
		accum.add(t1-t0)

# ------------------------------------------------------------------------------
# AccumulatorMonitor
#
# This class implements a thread-safe accumulator.

class AccumulatorMonitor:
	def __init__(self):
		self.accum = 0
		self.lock = threading.Lock()
		
	def add(self,value):
		self.lock.acquire()
		self.accum += value
		self.lock.release()
		
	def get(self):
		self.lock.acquire()
		total = self.accum
		self.lock.release()
		return total
	
################################################################################
# Define Experiment Parameters                                                 #
################################################################################

N  = 1024 # max buffer size
IT = 10   # averaging iterations

cbm = pycbm.pycbm(); # initialize the python interface to libcbm

job_list = dict()
job_list["popcnt"]         = [BenchmarkJob(cbm.popcnt32n, N)]
job_list["bitrev"]         = [BenchmarkJob(cbm.bitrev32n, N)]
job_list["ffs"]            = [BenchmarkJob(cbm.ffs32n,    N)]
job_list["popcnt/popcnt"]  = [BenchmarkJob(cbm.popcnt32n, N), \
                              BenchmarkJob(cbm.popcnt32n, N)]
job_list["popcnt/bitrev"]  = [BenchmarkJob(cbm.popcnt32n, N), \
                              BenchmarkJob(cbm.bitrev32n, N)]
job_list["popcnt/ffs"]     = [BenchmarkJob(cbm.popcnt32n, N), \
                              BenchmarkJob(cbm.ffs32n, N)]

################################################################################
# Run The Experiment                                                           #
################################################################################

# initialize y_data lists
y_data = dict()
for job_names in job_list.keys():
	y_data[job_names] = []

x_data = []

# process the job list
for i in range(N):
	x_data.append(4*(i+1)) # i words = 4i bytes
	
	for job_name in job_list.keys():
		accum = AccumulatorMonitor()
		
		threads = []
		for job in job_list[job_name]:
			t = threading.Thread(target=job.execute, args=(i+1,IT,accum))
			threads.append(t)
			t.start()
		for t in threads:
			t.join()
		
		# save in units of micro-seconds
		avg_etime = 1e6*(accum.get())/IT
		y_data[job_name].append(avg_etime)

fig, tgraph = plt.subplots()
tgraph.set_title("Avg Execution Time vs. Buffer Size")
tgraph.set_xlabel("Buffer Size (bytes)")
tgraph.set_ylabel("Avg Execution Time (micro-seconds)")

for key in y_data.keys():
	tgraph.plot(np.array(x_data),np.array(y_data[key]), label=key)
	
legend = tgraph.legend(loc='upper center', shadow=True)
plt.show()


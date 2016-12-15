################################################################################
# File  : test_libcbm.py                                                       #
# Brief : This script tests functions within libcbm.                           #
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

import pycbm
import array

popcnt_buff_in  = array.array('I', [0,1,3,7,15,0x55555555])
popcnt_buff_out = array.array('I', [0,0,0,0,0,0])

bitrev_buff_in  = array.array('I', [0x55555555,0xAAAAAAAA,0x00000001,0x80000000])
bitrev_buff_out = array.array('I', [0,0,0,0])

ffs_buff_in  = array.array('I', [0x00000000,0x00000001,0x00000002,0x00000004,0x80000000])
ffs_buff_out = array.array('I', [0,0,0,0,0])

lib = pycbm.pycbm();

lib.popcnt32n(popcnt_buff_in, popcnt_buff_out)
lib.bitrev32n(bitrev_buff_in, bitrev_buff_out)
lib.ffs32n(ffs_buff_in, ffs_buff_out)

print("Pop-Count Results:")
for (word_in,word_out) in zip(popcnt_buff_in,popcnt_buff_out):
	print("0x%.8X -> %i" % (word_in,word_out))

print("Bit-Reversal Results:")
for (word_in,word_out) in zip(bitrev_buff_in,bitrev_buff_out):
	print("0x%.8X -> 0x%.8X" % (word_in,word_out))
	
print("Find-First-Set Results:")
for (word_in,word_out) in zip(ffs_buff_in,ffs_buff_out):
	print("0x%.8X -> %i" % (word_in,word_out))
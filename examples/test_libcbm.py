import sys

# add a directory to the module search paths for pycbm
sys.path.append("../module")

import pycbm
import array

popcnt_buff_in  = array.array('I', [1,3,7,15,0x55555555])
popcnt_buff_out = array.array('I', [0,0,0,0,0])

bitrev_buff_in  = array.array('I', [0x55555555,0xAAAAAAAA,0x00000001,0x80000000])
bitrev_buff_out = array.array('I', [0,0,0,0])


lib = cbm.cbm();

lib.popcnt32n(popcnt_buff_in, popcnt_buff_out)
lib.bitrev32n(bitrev_buff_in, bitrev_buff_out)

print("Pop-Count Results:")
print(popcnt_buff_out)

print("Bit-Reversal Results:")
for word in bitrev_buff_out:
	print("0x%.8X" % word)
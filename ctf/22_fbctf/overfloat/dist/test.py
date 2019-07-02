from pwn import *

#e = ELF("./overfloat")
libc = ELF("./libc-2.27.so")
p = process("./overfloat")

print hex(next(libc.search("/bin/")))
#print next(p.search("/bin/"))

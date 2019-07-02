from pwn import *

e = ELF("./chall")

for symbol in e.symbols:
	print symbol, "\t", e.symbols[symbol]

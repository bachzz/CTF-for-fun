from pwn import *
import os

for i in range(0, 27):
	for j in range(0, 100):
		filename = './OUT/'+str(i)+'/'+str(j)
		cmd = "cat " + filename + " | grep ctf{"
		print filename
		os.system(cmd)

from pwn import *
from libformatstr import *

bufsiz = 100

p = process(['./format1_32',make_pattern(bufsiz)]) 

#output = p.recv().split()
#print output

data = p.recv()#output[0]      
#print data 
print guess_argnum(data, bufsiz)              
offset, padding = guess_argnum(data, bufsiz)

print offset, padding

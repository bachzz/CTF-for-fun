import base64
import os

filepath = 'nhatkycuame'  
with open(filepath) as fp:  
   line = fp.readline()
   while line:
       line = line.split("\n")[0]
       line = base64.b64decode(line)
       print line
       cmd = "echo "+line+" >> lyrics.txt"
       os.system(cmd)
       line = fp.readline()

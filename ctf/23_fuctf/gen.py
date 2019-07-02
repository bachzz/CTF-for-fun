MAX_DEPTH=5
MAX_LENGTH=4
import os, sys
import random
import string
def randomString(stringLength=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

depth=0
def gen(path,level):
	global depth
	for i in range(0,MAX_LENGTH):
		createPath=path+"/"+randomString(4)
		os.mkdir(createPath)

		if (level==MAX_DEPTH):
			return
		gen(createPath,level+1)



gen("./maze",0)

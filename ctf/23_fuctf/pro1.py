#print "a",
#print "b"
with open('hoctiengmeo.cpp'  ) as fp:  
	line = fp.readline()
	while line:
		tokens = line.split()
		#print tokens
		for token in tokens:
			with open('meow.h'  ) as fp2:  
				line2 = fp2.readline()
				while line2:
					line2 = line2.split("\n")[0]
					if token in line2:
						print line2.split(" ",2)[2],
					line2 = fp2.readline()
		print ""
		line = fp.readline()

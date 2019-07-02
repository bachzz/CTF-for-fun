#f = open("thuchanh.jpg","rb")
#f1 = open("ketqua0.jpg","wb")
f = open("result.jpg","rb")
f1 = open("result1.jpg","wb")

buf = f.read(2)
print buf
f1.write(buf)
buf = f.read(8)
print buf
nd = "this is flag"

def check(string):
	while len(string) < 8:
		string = ''.join(['0',string])
	return string


for i in nd:
	enc = bin(ord(i))[2:]
	enc = check(enc)
	#print enc
	number = 0
	for j in buf:
		dec = bin(ord(j))[2:]
		dec = check(dec)
		dec = dec[0:7]+enc[number]
		#print dec	
		number +=1
		ghifile = chr(int(dec,2))
		print ghifile

		f1.write(ghifile)
	buf = f.read(8)

while buf != "":
	for j in buf:
			dec = bin(ord(j))[2:]
			dec = check(dec)
			ghifile = chr(int(dec,2))

			f1.write(ghifile)
	buf = f.read(8)


f.close()
f1.close()


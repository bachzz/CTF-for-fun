letter = "abcdefghijklmnopqrstuvwxyz"
faces = ["=]]",":')",":0","_._!", ":'(",";]","=))","=)",":~)","(-_-)","-_-",":))","~_~","<3",":/","^_^",";))","*_*",":)","-.-","^^",":()",";)","@@",":>",":v"]

#filename = "faces.txt"
filename = "challenge.txt"
with open(filename, "r") as file:
    data = file.read()
for i in range(len(faces)):
    print (letter[i], faces[i])
    data = data.replace(faces[i], letter[i])

print (len(letter), len(faces))
print (data)

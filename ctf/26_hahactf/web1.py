arr = ["a", "3", "e", "w", "o", "n", "s", "r", "t", "1", "z", "f", "7", "k", "m", 'd', 'h'];
wellplayed = "";
for i in range(1,13):
    if i % 4 == 0:
     wellplayed += arr[i - 2]
    else:
     wellplayed += arr[i + 2]
print wellplayed

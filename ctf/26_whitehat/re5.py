n = 50
tmp_list = [True]*50
for i in xrange(3,int(pow(n,0.5))+1,2):
    if tmp_list[i]:
        tmp_list[i*i::2*i]=[False]*(((n-i*i-1)/(2*i))+1)
List = []
for i in xrange(3,50,2):
    if tmp_list[i]:
        List.append(i)
List = [2] + List
challenge = ['t','w','o','d','u','e','t','_','q','k','j','h','z','u','v','c','l','h','z','e','w','y','h','z','g','c','n','i','o','_','p','b','i','r','d','v','d','y','y','q','o','t','p','e','q','n','r','c','u','q']
flag = raw_input("Give me your flag: ")
flag = flag[-7:] + flag[:-7]
tmp_str = ''
for item in List:
    tmp_str += challenge[item]
print tmp_str
if flag == tmp_str:
    print flag, tmp_str
    print "Congratulation! Submit your flag"
else:
    print "Try your best, the rest will come"

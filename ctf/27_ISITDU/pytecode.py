flag = []

def checking_func() : 
    check = 0 
    if ord(flag[0]) + 52 != ord(flag[-1])  and ord(flag[-1]) - 4 != ord(flag[7]): 
        Fail() 
        exit(0) 
    if flag[:7] != "ISITDTU" : 
        exit(0) 
    if flag[9] != flag[14] and flag[14] != flag[19] and flag[19] != flag[24] : 
        check = 1 
        exit(0) 
    if ord(flag[8]) != 49 and flag[8] != flag[9] : 
        Fail() 
    if flag[10:14] != 'd0nT' : 
        # fail
        Fail() 
    if int(flag[18]) + int(flag[23]) + int(flag[28]) != 9 and flag[18] != flag[28]:
        # fail
        Fail() 
    if flag[15] != 'L' : 
        # fail 
        Fail()
    if ord(flag[17]) ^ -10 != -90 : 
        # fail 
        Fail()
    if ord(flag[20]) + 2 != ord(flag[27]) and ord(flag[27]) > 123 and ord(flag[20]) < 97 : 
        # fail 
        Fail()
    if ord(flag[27]) != 100 : 
        #fail 
        Fail()
    if flag[25] != 'C' : 
        # fail 
        Fail()
    if ord(flag[26]) % 2 != 0 and ord(flag[26]) % 3 != 0 and ord(flag[26]) % 4 != 0 and flag[26].isdigit() : 
        # fail 
        Fail()
    if int(flag[23]) != 3 : 
        # fail 
        Fail()
    if flag[22] < flag[13] : 
        # fail 
        Fail()    
    tmp = 0 
    for i in flag : 
        tmp += ord(i) 
    if tmp != 2441 :
        Fail() 
        # fail 
    Correct()

 
def Fail() : 
    print 'Bye!!!'
def Correct() : 
    print 'Wow!!!You so best^_^'

flag = list(raw_input())
print flag
checking_func()

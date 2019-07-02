
def strongAchilliesNumber():
    c =0
    strongAchilliescounter = 0
    a = input("Enter the lower limit (must be >= 1)")
    b = input("Enter the upper limit(must be <= 10^8)")
    def checkPrime(numb):
        prime = True
        for i in range(numb/2):
            i = i+2
            if numb%i == 0:
                prime = False
                break
        if numb == 2:
            return True
        else:           
            return prime
   
    def calculatePhiNumber(number):
        phiNumber = 1
        for i in range(number/2):
            i = i+2
            powr = 0
            if checkPrime(i) == True and number % i == 0:
                powr = powr+1
                numb = number/i 
                while numb % i == 0:
                    powr = powr+1
                    numb = numb/i
                phiNumber = phiNumber*(pow(i,powr)-pow(i,powr-1))
        return phiNumber
                            
    def checkPowerful(number):
        powerful = True   
        phiNumber = 1   
        powr = 0
        powersList = ()
        maxPower = 0
        for i in range(number/2):
            i = i+2
            powr = 0
            if checkPrime(i) == True and number % i == 0:
                #print i
                powr = powr+1
                numb = number/i 
                while numb % i == 0:
                    powr = powr+1
                    numb = numb/i
                if maxPower < powr:
                    maxPower = powr
                powersList = powersList+(powr,)
                if powr < 2:
                    powerful = False
                    break
        #print powersList,maxPower           
        if powerful == False:
            return False
        else:
            perfect  = True   
            for l in range(maxPower-1):
                l = l+2
                #print ">",l
                temp = True
                for p in powersList:
                    if p%l != 0:        
                        temp = False
                if temp == False:
                    perfect = False
                else:
                    perfect = True
                    break
            if perfect == False:
                return True
            else:
                return False
    for i in range(b):           
        number = i+a
        if checkPowerful(number) == True:
            if checkPowerful(calculatePhiNumber(number)) == True:
                strongAchilliescounter = strongAchilliescounter + 1
                c = c+1
                print number,"is a Strong Achilles number:" + str(c)
            else:
                c=c+1
                print number,"is an Achilles number but not a Strong Achillies number:" + str(c)
                continue   
        else:
            #print number,"is not an Achilles number:"
            continue
    print "Total number of Strong Achilles number is:",strongAchilliescounter                           
strongAchilliesNumber()

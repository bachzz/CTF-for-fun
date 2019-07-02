'''def isPrime(num):
  if num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           #print(num,"is not a prime number")
           #print(i,"times",num//i,"is",num)
           return 1
  return 0

def isPrime(l): #Create a function for the test
    if l==2: return 1#quit("\n Two is the only even prime number.") #An exception for 2
    if l%2==0: return 0#quit("\n Even.") #Check if X is even(including negative numbers)
    if l<0: return 0 #An exception for negative odd numbers to end the function with False
    if l==1: return 0#quit("\n One is neither composite nor prime.") #An exception for 1
#Trial division
    for i in range(3,int(round(l**(1/2)))+1,2):  #Loop for i: all odd numbers from 3 to sqrt(X)
        if l%i==0: return 0 #Check if X is divisible by any of the values of i and end the function with False
    return 1 #If the loop finishe, i.e. X isn't divisible by anything, end the function with True
from math import sqrt; from itertools import count, islice

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def isPrime(a):
    return all(a % i for i in xrange(2, a))'''
import math

def isPrime(n):
    if n == 2:
        return 1
    if n % 2 == 0 or n <= 1:
        return 0

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return 0
    return 1

def intToList(number):
  b = str(number)
  c = []

  for digit in b:
    c.append (int(digit))

  return c


def isBeautiful(number):
	numberLst = intToList(number)	
	
	for i in range(0, len(numberLst)):
		if numberLst[i] != numberLst[-i-1]:
			return 0
	return 1

count = 0
for number in range(4256, 61529):
	if isPrime(number) and isBeautiful(number):
		print(number)
		count= count+1

print(count) 

# Program to check if the given number
# is an Achilles Number
from math import sqrt, log

# function to check if the number
# is powerful number
def isPowerful(n):

# First divide the number repeatedly by 2
while (n % 2 == 0):
power = 0
while (n % 2 == 0):
n /= 2
power += 1

# If only 2^1 divides n (not higher
# powers), then return false
if (power == 1):
return False

# if n is not a power of 2 then this
# loop will execute repeat above process
p = int(sqrt(n)) + 1
for factor in range(3, p, 2):


# Find highest power of “factor”
# that divides n
power = 0
while (n % factor == 0):
n = n / factor
power += 1

# If only factor^1 divides n (not higher
# powers), then return false
if (power == 1):
return False

# n must be 1 now if it is not a prime number.
# Since prime numbers are not powerful, we
# return false if n is not 1.
return (n == 1)

# Utility function to check if
# number is a perfect power or not
def isPower(a):
if (a == 1):
return True

p = int(sqrt(a)) + 1

for i in range(2, a, 1):
	val = log(a) / log(i)
	if ((val – int(val)) < 0.00000001): 
		return True 
	return False # Function to check Achilles Number def isAchillesNumber(n): if (isPowerful(n) == True and isPower(n) == False): return True else: return False # Driver Code if __name__ == '__main__': n = 72 if (isAchillesNumber(n)): print("YES") else: print("NO") n = 36 if (isAchillesNumber(n)): print("YES") else: print("NO") # This code is contributed by # Surendra_Gangwar [tabby title="C#"] 

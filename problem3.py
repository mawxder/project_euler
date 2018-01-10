# What is the largest prime factor of the number 600851475143

# Set variables
number = 600851475143
primeList = []
primeFactorList = []

# Make list of prime numbers < 'number'
for x in range(2, number+1):
    isPrime = True
    # Don't calculate for more than the sqrt of number for efficiency
    for y in range(2, int(x**0.5)+1):
        if x % y == 0:
            isPrime = False
            break
    if isPrime:
        primeList.append(x)

# Iterate over primeList to check for prime factors of 'number'
for i in primeList:
    if number % i == 0:
        primeFactorList.append(i)
        
# Print largest prime factor of number
print(max(primeFactorList))

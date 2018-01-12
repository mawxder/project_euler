# What is the largest prime factor of the number 600851475143
import time
t1 = time.clock()

# Set variables
number = 600851475143
primeFactorList = []

def primeList(number):
    # Make list of prime numbers < 'number'
    for x in range(2, number+1):
        isPrime = True
        # Don't calculate for more than the sqrt of number for efficiency
        for y in range(2, int(x**0.5)+1):
            if x % y == 0:
                isPrime = False
                break
        if isPrime:
            yield x

# Calculate  primes using primeList and check for prime factors of 'number'
for i in primeList(number):
    if i > number**0.5:
        break
    if number % i == 0:
        primeFactorList.append(i)

# Print largest prime factor of 'number'
print(max(primeFactorList))
t2 = time.clock()

print('Took {} seconds'.format(t2-t1))

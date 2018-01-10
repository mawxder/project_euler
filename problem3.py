# What is the largest prime factor of the number 600851475143

number = 600851475143

primeList = []
primeFactorList = []
for x in range(2, number+1):
    isPrime = True
    for y in range(2, int(x**0.5)+1):
        if x % y == 0:
            isPrime = False
            break
    if isPrime:
        primeList.append(x)
        print(x)

for i in primeList:
    if number % i == 0:
        primeFactorList.append(i)
        print(i)

print(max(primeFactorList))

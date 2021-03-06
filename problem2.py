# By considering he terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.
# Each new term in the Fibonacci sequence is generated by adding the previous two terms.

a, b = 0, 1
storage = 0
# FIbonacci sequence using multiple assignent:
# https://stackoverflow.com/a/18009977/9185666
while b < 4000000:
    # Multiple assignment, atomic version of:
    # a = b
    # b = a + b
    a, b = b, a+b
    if (b%2 == 0):
        storage += b

print(storage)

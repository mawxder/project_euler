# Find the sum of all the multiples of 3 or 5 below 1000.
storage = 0
for element in range(1, 1000 + 1):
    if (element%3 == 0) or (element%5 == 0):
        storage = storage + element
print(storage)

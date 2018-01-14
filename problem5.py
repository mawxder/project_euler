# What si the smallest positive number that is evenly divisible by all of the numbers from 1 to 20
import sys
import time

# Define function (generator)
def smallest_multiple():
    # Range from 20 to infinity going 2 by 2 because odd numbers are already not divisible by even numbers
    for x in range(20, sys.maxsize**10, 2):
        storage = 0
        # Check if remaider of all 1 to 20 numbers equals zero
        for y in range(1, 21):
            if x%y == 0:
                # Set counter
                storage += 1
        if storage == 20:
            yield x
            break
t1 = time.clock()
# Print firss (next / smallest)
print(next(smallest_multiple()))
t2 = time.clock()
print(t2-t1)

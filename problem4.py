# Find the largest palindrome made from the product of two 3-digit numbers.

# Set variables
number_1 = []
number_2 = []
storage = []

# Iterate over one 3-digit number
for x in range(100, 1000):
    # Iterate over a second 3-digit number
    for y in range(100, 1000):
        product = x * y
        # Test whether the product number is a palindrome
        if str(x * y) == str(product)[::-1]:
            # Append palindromes to 'storage'
            storage.append(x * y)
# Print largest
print(max(storage))

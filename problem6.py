# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

square_of_sum = sum([x for x in range(1, 100+1)])**2
sum_of_squares = sum([x**2 for x in range(1, 100+1)])

print(square_of_sum - sum_of_squares)

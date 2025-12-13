'''
The sum of the squares of the first ten natural numbers is,
1² + 2² + ... + 10² = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)² = 55² = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

def solve(n):
    sum_n = n * (n + 1) // 2
    sum_of_squares = n * (n + 1) * (2 * n + 1) // 6
    square_of_sum = sum_n ** 2

    difference = square_of_sum - sum_of_squares
    return difference, sum_of_squares, square_of_sum

# Test with n=10
diff_10, sum_sq_10, sq_sum_10 = solve(10)
print(f"for n=10:")
print(f"  sum of squares: {sum_sq_10}")
print(f"  square of sum: {sq_sum_10}")
print(f"  difference: {diff_10}")
print()

# Solve for n=100
diff_100, sum_sq_100, sq_sum_100 = solve(100)
print(f"for n=100:")
print(f"  sum of squares: {sum_sq_100}")
print(f"  square of sum: {sq_sum_100}")
print(f"  difference: {diff_100}")
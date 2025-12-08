"""
A number is a perfect square, or a square number, if it is the square of a positive integer.
For example, 25 is a square number because 5^2 =5 x 5 =25; it is also an odd square.

The first 5 square numbers are: 1,4,9,16,25, and the sum of the odd squares is 1 +9 +25 =35.

Among the first 854 thousand square numbers, what is the sum of all the odd squares?
"""

count = 0
for i in range(1, 854000):
    sum = i**2
    print(sum)
    if sum % 2 == 1:
        count += sum
print(count)

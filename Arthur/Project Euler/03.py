# This one killed me, I tried sieve first but very quickly hit insufficient
# memory. Had to use a bytearray, but this method is far simpler and hugely
# improves space complexity. The reducing of maximum also hugely improves
# time complexity, but it is still O(sqrt(n)) worst case.

maximum = 600_851_475_143

n = 2
while n*n <= maximum:
    while maximum % n == 0:
        maximum //= n
    n += 1

print(maximum)

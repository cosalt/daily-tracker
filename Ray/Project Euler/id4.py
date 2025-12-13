'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009.

Find the largest palindrome made from the product of two 3-digit numbers.

Mathematical approach:
- 6-digit palindrome: abccba = 100001a + 10010b + 1100c = 11(9091a + 910b + 100c)
- Therefore, any 6-digit palindrome is divisible by 11
- So at least one of our factors must be divisible by 11
- We search from largest to smallest for efficiency
'''

def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

# Start from the largest 3-digit number and work down
# At least one factor must be divisible by 11 for 6-digit palindromes
largest_palindrome = 0

# Iterate with i starting from 999 down
for i in range(999, 99, -1):
    # j starts from i and decrements (avoid duplicate checks like 999*998 and 998*999)
    for j in range(i, 99, -1):
        product = i * j
        
        # Early termination: if current product is less than largest found, 
        # no need to continue with smaller j values for this i
        if product <= largest_palindrome:
            break
            
        if is_palindrome(product):
            largest_palindrome = product

print(f"The largest palindrome from the product of two 3-digit numbers is: {largest_palindrome}")
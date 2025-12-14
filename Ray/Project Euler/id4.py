'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009.

Find the largest palindrome made from the product of two 3-digit numbers.

'''

def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

largest = 0

for i in range(999, 99, -1):
    for j in range(i, 99, -1):
        product = i * j
        if product <= largest:
            break
            
        if is_palindrome(product):
            largest = product

print(f"3digit: {largest}")
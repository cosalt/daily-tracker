'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
'''

import math

def est(n):
    if n < 6:
        return 15
    
    ln_n = math.log(n)
    ln_ln_n = math.log(ln_n)
    estimate = int(n * (ln_n + ln_ln_n) * 1.15)
    return estimate

def soe(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, limit + 1, i):
                sieve[j] = False
    
    return [i for i in range(2, limit + 1) if sieve[i]]

def nprime(n):
    limit = est(n)
    primes = soe(limit)
    
    while len(primes) < n:
        limit = int(limit * 1.5)
        primes = soe(limit)
    
    return primes[n - 1]

print(f" 6th prime is: {nprime(6)}")

result = nprime(10001)
print(f" 10001st prime number is: {result}")

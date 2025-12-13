'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

lcm
'''

def get_primes(n):
    #sieve of eratosthenes
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n + 1, i):
                sieve[j] = False
    
    return [i for i in range(n + 1) if sieve[i]]

def lcm_range(n):
    primes = get_primes(n)
    result = 1
    
    for prime in primes:
        power = 1
        while prime ** (power + 1) <= n:
            power += 1
        result *= prime ** power
    
    return result

answer = lcm_range(20)
print(f"{answer}")

print("\ncheck:")
for i in range(1, 21):
    if answer % i == 0:
        print(f"✓ {answer} ÷ {i} = {answer // i}")
    else:
        print(f"✗ {answer} n ot divisible by {i}")
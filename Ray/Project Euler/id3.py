"""The prime factors of 13195 are 5,7,13 and 29.

What is the largest prime factor of the number 600851475143?"""



def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
    return True

def largest_prime(num):
    for i in range(num, 2, -1):
        if is_prime(i):
            return True
    else:
        return False
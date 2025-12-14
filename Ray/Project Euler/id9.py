"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a² + b² = c²
For example, 3² + 4² = 9 + 16 = 25 = 5².
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def find_pythagorean_triplet():
    for a in range(1, 334):
        if a == 1000:
            continue
            
        numerator = 1000 * a - 500000
        denominator = a - 1000
        
        if numerator % denominator == 0:
            b = numerator // denominator
            c = 1000 - a - b            
            if a < b < c and a * a + b * b == c * c:
                return a, b, c
    
    return None

result = find_pythagorean_triplet()

if result:
    a, b, c = result
    product = a * b * c
    print(f"py triplet: a = {a}, b = {b}, c = {c}")
    print(f"{c}² = {c*c}")
    print(f"sum: {a} + {b} + {c} = {a + b + c}")
    print(f"\nproduct abc = {product}")
else:
    print("no found")
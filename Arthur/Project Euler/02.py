limit = 4_000_000

sum = 0 
fib_a, fib_b = 0, 2

while fib_b <= limit:
    sum += fib_b 
    fib_a, fib_b = fib_b, 4*fib_b+fib_a

print(sum)


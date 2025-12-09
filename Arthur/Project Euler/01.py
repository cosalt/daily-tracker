max_val = 1000
m1 = 3
m2 = 5

def sum_multiples(val, maximum):
    count = (maximum - 1) // val
    return val * (count * (count + 1) // 2)

def lcm(n1, n2):
    multiple = n1 if n1 >= n2 else n2
    while True:
        if multiple % n1 == 0 and multiple % n2 == 0:
            return multiple
        multiple += 1

total = sum_multiples(m1, max_val) + sum_multiples(m2, max_val) - sum_multiples(lcm(m1, m2), max_val)

print(total)

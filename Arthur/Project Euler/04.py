def maxPalindrome(digits):
    minimum = 10**(digits-1)-1 
    maximum = 10**digits-1

    res = -1
    for n1 in range(maximum, minimum, -1):
        if n1*maximum < res:
            break
        for n2 in range(maximum, n1, -1):
            prod = n1*n2
            if prod < res:
                break
            if str(prod) == str(prod)[::-1]:
                res = prod
            n2 += 1
        n1 += 1

    return res

print(maxPalindrome(3))


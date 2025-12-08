'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3,5,6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''
def fib(n):

    if n in [1,2]:
        return 1

    return (fib(n-1) + fib(n-2))
sum = 0    
for i in range(2,1000):
    if fib(i) < 4000000:
        if (fib(i)%2) == 0:
            sum += fib(i)
    else:
        break
print(sum)
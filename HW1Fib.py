def rFib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return rFib(n-1) + rFib(n-2)


def iFib(n):
    fib = 0
    a = 1
    t = 0
    for x in xrange(n):
        t = fib + a
        a = fib
        fib = t

    return fib

print [0,1,1,2,3,5,8,13,21]
print [rFib(n) for n in range(9)]
print [iFib(n) for n in range(9)]

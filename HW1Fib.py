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

nset = [5, 10, 15, 20, 30, 50, 100,1000, 2000, 5000, 10000]


from time import clock
def timefunc(func,arg):
    startTime = clock()
    func(arg)
    return clock()-startTime

#recurstimes = [timefunc(rFib,n) for n in nset]
#itertimes = [timefunc(iFib,n) for n in nset]
recurstimes, itertimes = [] ,[]

for n in nset:
    recurstimes.append(timefunc(rFib,n))
    itertimes.append(timefunc(iFib,n))
    print n," -> r:",recurstimes
    print n," -> i:",itertimes
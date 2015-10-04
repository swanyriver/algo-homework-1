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
    return round(clock()-startTime,3)

itertimes = [timefunc(iFib,n) for n in nset]
print itertimes
#recurstimes = [timefunc(rFib,n) for n in nset[:6]]
#print recurstimes

for i in xrange(1000):
    print "recursfib:%d, time%f"%(i,timefunc(rFib,i))

# for n in nset:
#     recurstimes.append(timefunc(rFib,n))
#     itertimes.append(timefunc(iFib,n))
#     print n," -> r:",recurstimes
#     print n," -> i:",itertimes
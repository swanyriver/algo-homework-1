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

def iFib2(n):
    fib = 0
    prev = 1

    for x in xrange(n):
        prev,fib = fib,fib+prev

    return fib

nset = [10, 15, 20, 30, 50, 100,1000, 2000, 5000, 10000]


from time import clock
def timefunc(func,arg,t):
    startTime = clock()
    for x in xrange(t):func(arg)
    return round(clock()-startTime,5)

#itertimes = [timefunc(iFib,n) for n in nset]
#print itertimes
#recurstimes = [timefunc(rFib,n) for n in nset[:6]]
#print recurstimes

# for i in xrange(1000):
#     print "recursfib:%d, time%f"%(i,timefunc(rFib,i))

# for n in nset:
#     recurstimes.append(timefunc(rFib,n))
#     itertimes.append(timefunc(iFib,n))
#     print n," -> r:",recurstimes
#     print n," -> i:",itertimes

print "n,Time"
for n in range(10,50):
#for n in nset:
    print n, "," ,timefunc(rFib,n,1)



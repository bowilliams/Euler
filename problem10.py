def is_prime(n):
    if n == 2:
        return True
    if n == 0 or n % 2 == 0:
        return False
    for x in xrange(3, int(n**0.5)+1, 2):
        if n%x == 0:
            return False
    return True

print 2+reduce((lambda x,y: x+y),[x for x in xrange(3,2000000,2) if is_prime(x)])

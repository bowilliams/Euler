import sys
def is_prime(n):
    if n == 0 or n % 2 == 0:
        return False
    for x in xrange(3, int(n**0.5)+1, 2):
        if n%x == 0:
            return False
    return True

count = 1
for x in xrange(2,sys.maxint):
    if is_prime(x):
        count = count + 1
    if count == 10001:
        print x
        sys.exit()

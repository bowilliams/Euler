import math
n = 600851475143

def get_factors(n):
    factors = []
    for x in xrange(2,int(math.ceil(math.sqrt(n)))):
        if (n % x == 0):
            factors.append(x)
    return factors

for x in get_factors(n):
    if len(get_factors(x)) < 1:
        print x

    




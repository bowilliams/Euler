import sys
def is_match(a,b,c):
    return a**2 + b**2 == c**2

candidates = []
for a in xrange(1,999):
    for b in xrange(1,999):
        for c in xrange(1,999):
            if a+b+c == 1000 and is_match(a,b,c):
                print a*b*c
                sys.exit()

#v1
total = 0
for i in xrange(1,1000):
    if (i % 3 == 0 or i % 5 == 0):
        total += i
print total

#v2
print sum([x for x in xrange(1,1000) if x % 3 == 0 or x % 5 == 0])

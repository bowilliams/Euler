sumSquares = reduce((lambda x,y: x+y), [x**2 for x in xrange(1,101)])
sum100 = reduce((lambda x,y: x+y), [x for x in xrange(1,101)])
print sum100**2 - sumSquares

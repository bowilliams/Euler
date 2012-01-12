import time
start = time.clock()
print str(start)
x = 1
y = 2
sum = 2
i = 0
seq = "1,2"
while ((x+y) < 4000000):
    i = x + y
    x = y
    y = i
    if (i % 2 == 0):
        sum += i
end = time.clock()
print str(end-start) + 'ms'
print sum

# optimization - after 2, every third term is an even term. can we just skip to those?
start = time.clock()
sum = 0
a=1
b=1
c=a+b
while (c<4000000):
    sum += c
    a = b+c
    b = a+c
    c = a+b
end = time.clock()
print str(end-start) + 'ms'
print sum





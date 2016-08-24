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
print sum

# optimization - after 2, every third term is an even term. can we just skip to those?





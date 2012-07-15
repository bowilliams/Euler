gotit = False
x = 0
test = 0

while not gotit:                         
    x += 1
    test = x*20
    gotit = True
    for y in reversed(xrange(2,20)):
        if test % y == 0:
            continue
        else:
            gotit = False
            break
print test

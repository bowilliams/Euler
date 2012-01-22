import sys
# pass a string, not an int
def is_palindrome(x):
    for index in xrange(0,len(str(x))/2):
        if x[index] != x[-index-1]:
            return False
    return True

largest = 0
for x in reversed(xrange(1,1000)):
    for y in reversed(xrange(1,1000)):
        if is_palindrome(str(x*y)) and (x*y > largest):
            largest = x*y
print largest

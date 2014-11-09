import math
 
def get_divisors(number):
    tlist = []
    for x in xrange(2, int(math.sqrt(number))):
        d,r = divmod(number,x)
        if r == 0:
            tlist.append(x)
            tlist.append(d)
 
    return len([1, number] + tlist)
 

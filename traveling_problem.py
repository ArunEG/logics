""" A man traveling from point (0,0) to different locations
like (2,1),(3,4),..(x,y)
if the man reaches at any previous locations program will stop   """
import sys


def Solution(**loc):
    """ funtion for searching previous locations """
    loc = dict(loc)
    if loc in loc_list:
        print "You Reached at your privious location"
        sys.exit()
    else:
        loc_list.append(loc)
        print loc_list


loc = {}
loc_list = []
print "Enter number of positions(x,y)"
n = input()
for i in xrange(1, n):
    print "Enter x value"
    key = input()
    print "Enter y value"
    loc[str(key)] = input()
    Solution(**loc)
    loc = {}
    print "\n"

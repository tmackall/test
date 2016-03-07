#!/usr/bin/python
'''
This was asked during my Teradata interview.
'''

import random


def prime_is_it(int_in):

    if int_in == 1:
        return True
    elif int_in == 0:
        return False

    # loop - all nums to input in
    for tv in xrange(2, int_in+1):
        if int_in % tv == 0 and int_in != tv:
            print tv
            return False

    return True


tsl = random.sample(xrange(2500), 50)
for ts in tsl:
    print 'input: %s - prime?: %s' % (ts, prime_is_it(ts))

exit(0)

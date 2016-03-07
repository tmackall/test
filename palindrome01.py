#!/usr/bin/python

import re


def palindrome_check(str_in):

    # lower-case - reduce it
    str_test = str_in.lower()

    # non-alpha - remove
    str_test = re.sub('[^a-z]', '', str_test)

    print str_test
    palindrome = ''
    # window start loop
    for wst in xrange(len(str_test)):

        pal_tmp = ''

        # window size loop
        for wsi in xrange(wst+1, len(str_test)+1):
            fwd = str_test[wst:wsi]
            bwd = fwd[::-1]
            if bwd == fwd and len(bwd) > len(pal_tmp):
                pal_tmp = bwd
                print '%s:%s' % (fwd, bwd)

        if len(pal_tmp) > len(palindrome):
            palindrome = pal_tmp

    return palindrome


tsl = []
tsl.append('SDLsdswekjui8t')
tsl.append('SD8Lsd')
tsl.append('Uabba')
tsl.append('A man, a plan, a canal, Panama!')
tsl.append('No \'x\' in NixonR')
for ts in tsl:
    print 'input: %s, largest palindrome: %s' % (ts, palindrome_check(ts))

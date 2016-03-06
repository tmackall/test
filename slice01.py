#!/usr/bin/python


#
# test string - create it ('01234567890')
test_str = ''
for i in xrange(10):
    test_str += str(i)

print 'test string: %s' % test_str

#
# slice - original string
print 'original string: %s' % (test_str[:3] + test_str[3:])

# reverse
print 'reverse: %s' % test_str[::-1]

# reverse - every other
print 'reverse every other: %s' % test_str[::-2]

# every other
print 'every other: %s' % test_str[::2]

# every third
print 'every third: %s' % test_str[::3]

# third character on
print 'third character on: %s' % test_str[2:]

# start to third character
print 'start to the third character: %s' % test_str[:3]

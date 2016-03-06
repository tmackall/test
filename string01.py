#!/usr/bin/python

#
# capitalize = Weassdwwwwww
ts = 'weASSDwwwwww'
print ts.capitalize()

# upper  = WEASSDWWWWWW
ts = 'weASSDwwwwww'
print ts.upper()

# lower  = weassdwwwwww
ts = 'weASSDwwwwww'
print ts.lower()

# split  - make list from commas =
# ['1997', 'Ford', 'E350', 'Super', ' luxurious truck']
ts = '1997,Ford,E350,Super, luxurious truck'
print ts.split(',')

# remove beginning and ending blanks (left strip and right strip)
ts = '  123456789   '
print ts.lstrip(' ')
print ts.rstrip(' ')

# count - substing instances
print ts.count(' ')  # 5
print ts.count('  ')  # 2

# digit?
ts = '1234'
print ts.isdigit()  # true
ts = '1234 '
print ts.isdigit()  # false

#
# join
val_join = ''
ts = ['1997', 'Ford', 'E350', 'Super', ' luxurious truck']
print val_join.join(ts)
val_join = '='
print val_join.join(ts)

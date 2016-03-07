#!/usr/bin/python

# I have an array of integer. That provides data to one of the UI screen.
# That UI screen can show at a time only one data. For each iteration on
# the array 3 elements get picked up however only the highest number out
# of those usually shows up on the UI.


tl = [1, 4, 5, 2, 3, 4, 5, 6]
win_size = 3

for i in xrange(len(tl)):
    win_list = tl[i:i+3]
    print max(win_list)

exit(0)

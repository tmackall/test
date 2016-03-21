'''
Tests
input -> output
-1 -> 11
0 -> 11
1 -> 11
5 -> 11
6 -> 11
10 -> 11
12 -> 22
13 -> 22
14 -> 22
1000 -> 1001
2001 -> 2002
3001 -> 3003
3002 -> 3003
3004 -> 3113
'a' -> exception
'''

def next_greatest_palindrome(input_number):

    try:
        int(input_number)
    except:
        print 'input needs to be integer'
        return -1

    num_str = str(input_number)

    if num_str == num_str[::-1]:
       return input_number

    np_count = input_number + 1

    while True:

        num_str = str(np_count)

        if num_str == num_str[::-1]:
            return np_count

        np_count += 1

print next_greatest_palindrome(3004)


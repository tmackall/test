#!/usr/bin/python
import sys


def prime_gen(num_primes):
    cnt = 0
    num_test = 2
    while cnt < num_primes:
        j = 2
        print 'cnt: {}'.format(cnt)
        while j <= num_test:
            print(j, num_test)
            if (num_test % j) == 0:
                if num_test == j:
                    cnt += 1
                    yield j
                else:
                    print 'not a prime number:{}'.format(num_test)
                num_test += 1
                break
            else:
                j += 1


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print '{} <number of primes>'.format(sys.argv[0])
        exit(1)

    print list(prime_gen(int(sys.argv[1])))

#! /usr/bin/python2.5 -tt

# Problem Set 1
# Name: Anna Liu
# Collaborators: N/A
# Time: 00:35:00
# Date: 20/03/2014

# compute up to the 10**5th Prime Number and print f(x)*ln(x)/x. 
# PNT states: f(x)*ln(x)/x = 1 as x -> infinity. 
# f(x) being the number of prime numbers less than x.
# test result: ratio = 1.0831.

import math

def main():

  odd_num = 3
  prime_count = 2
  while prime_count <= 100000:
    odd_num += 2
    divisor = 3
    while odd_num % divisor != 0 and divisor < odd_num / 3:
      divisor += 2
    if divisor >= odd_num / 3:
      prime_count += 1
      print 'ratio = ', prime_count * math.log(odd_num) / odd_num


if __name__ == '__main__':
  main()

#! /usr/bin/python2.5 -tt

# Problem Set 1
# Name: Anna Liu
# Collaborators: N/A
# Time: 00:10:00
# Date: 22/03/2014

# computes sum of logs for all primes less than n.
# print out sum of logs, n, and their ratio.
# the ratio should approximates to 1 according to number theory.


import math

def main():

  odd_num = 3
  prime_count = 2
  sum_of_logs = 3
  
  while prime_count <= 1000:
    odd_num += 2
    divisor = 3
    while odd_num % divisor != 0 and divisor < odd_num / 3:
      divisor += 2
    if divisor >= odd_num / 3:
      prime_count += 1
      sum_of_logs += math.log(odd_num)
      print 'sum of logs:', sum_of_logs, '\tn = ', odd_num, '\tratio = ', odd_num / sum_of_logs


if __name__ == '__main__':
  main()

#! /usr/bin/python2.5 -tt

# Problem Set 1
# Name: Anna Liu
# Collaborators: N/A
# Time: 00:35:00
# Date: 19/03/2014

# computes and print the 1000th prime number.

def main():
  odd_num = 3
  prime_count = 2
  while prime_count <= 1000:
    odd_num += 2
    divisor = 3
    while odd_num % divisor != 0 and divisor < odd_num / 3:
      divisor += 2
    if divisor >= odd_num / 3:
      prime_count += 1
  print odd_num


if __name__ == '__main__':
  main()

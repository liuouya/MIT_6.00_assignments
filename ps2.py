#! /usr/bin/python2.5 -tt

# Problem Set 2
# Name: Anna Liu
# Collaborators: N/A
# Time: 01:00:00
# Date: 29/03/2014


# print the combinations of (6, 9, 20) box needed
# for "total" number of McNuggets.

total = 55

def main():
  
  
  # compute all the possible combinations
  list = ()  
  for i in range(0, total/6+1):
    list += (i, 0, 0)
    for j in range(0, total/9+1):
      list += (i, j, 0)
      if i == list[-6] and j == list[-5]:
        list = list[:-3]
      for k in range(0, total/20+1):
        list += (i, j, k)
        if i == list[-6] and j == list[-5] and k == list[-4]:
          list = list[:-3]
          
  
  # check for valid combinations
  n = 0
  while (n < (len(list) - 3)):
    if (list[n]*6 + list[n+1]*9 + list[n+2]*20) == total:
      print list[n:n+3]
    n += 3


if __name__ == '__main__':
  main()


# number of 6, 9, 20 McNuggets box needed for a total of:
# 50 - (2, 2, 1)
# 51 - (1, 5, 0)
# 52 - (2, 0, 2)
# 53 - (1, 3, 1)
# 54 - (3, 4, 0)
# 55 - (1, 1, 2)

# if n to n+5 are possible then n+6 to n+11 are possible too
# just use solutions plus 1 more box of 6 and so on...

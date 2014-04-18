#! /usr/bin/python2.5 -tt

# Problem Set 2
# Name: Anna Liu
# Collaborators: N/A
# Time: 00:20:00
# Date: 29/03/2014

# find and print the biggest number of McNuggets
# that cannot be bought in box of 6, 9, 20


def main():
  
  # compute a list of all possible combinations
  
  list = ()
  
  for i in range(0, 55/6+1):
    list += (i, 0, 0)
    for j in range(0, 55/9+1):
      list += (i, j, 0)
      if i == list[-6] and j == list[-5]:
        list = list[:-3]
      for k in range(0, 55/20+1):
        list += (i, j, k)
        if i == list[-6] and j == list[-5] and k == list[-4]:
          list = list[:-3]

  # search for valid combination for 50-i McNuggets
  
  for i in range(0, 50):
    n = solution = 0
    while (n < (len(list) - 3)):
      if (list[n]*6 + list[n+1]*9 + list[n+2]*20) == (50 - i):
        solution = 1
      n += 3
    if solution == 0:
      print 'Largest number of McNuggets that cannot be bought in exact quantity:', 50 - i
      break


if __name__ == '__main__':
  main()

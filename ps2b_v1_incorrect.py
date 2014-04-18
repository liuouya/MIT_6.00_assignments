#! /usr/bin/python2.5 -tt

# Problem Set 2
# Name: Anna Liu
# Collaborators: N/A
# Time: 00:20:00
# Date: 29/03/2014

# search and print the largest number of McNuggets
# that cannot be bought in combination of "box_size"

#incorrect: doesn't work for cases like (x, 2x, 3x)

box_size = (6, 9, 20)
top_lim = 200

def main():
  
  # compute a list of all possible combinations
  
  list = ()
  
  for i in range(0, top_lim/box_size[0]+1):
    list += (i, 0, 0)
    for j in range(0, top_lim/box_size[1]+1):
      list += (i, j, 0)
      if i == list[-6] and j == list[-5]:
        list = list[:-3]
      for k in range(0, top_lim/box_size[2]+1):
        list += (i, j, k)
        if i == list[-6] and j == list[-5] and k == list[-4]:
          list = list[:-3]

  # search for valid combination for top_lim - i McNuggets
  
  for i in range(0, top_lim):
    n = solution = 0
    while (n < (len(list) - 3)):
      if (list[n]*box_size[0] + list[n+1]*box_size[1] + list[n+2]*box_size[2]) == (top_lim - i):
        solution = 1
      n += 3
    if solution == 0:
      print 'Given package sizes', box_size[0], box_size[1], 'and', box_size[2], 'the largest number of McNuggets that cannot be bought in exact quantity is:', top_lim-i
      break
    
  if solution != 0:
    print 'Given package sizes', box_size[0], box_size[1], 'and', box_size[2], 'you can buy any number you want.'


if __name__ == '__main__':
  main()

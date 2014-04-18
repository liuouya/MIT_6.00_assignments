#! /usr/bin/python2.5 -tt

# Problem Set 2
# Name: Anna Liu
# Collaborators: N/A
# Time: 00:20:00
# Date: 01/04/2014

# search and print the largest number of McNuggets
# that cannot be bought in combination of box_size(x,y,z)

box_size = (6, 9, 20)
top_lim = 200


# compute list of all possible combinations
def make_list(total_num):
  list = ()
  for i in range(0, total_num/box_size[0]+1):
    list += (i, 0, 0)
    for j in range(0, total_num/box_size[1]+1):
      list += (i, j, 0)
      if i == list[-6] and j == list[-5]:
        list = list[:-3]
      for k in range(0, total_num/box_size[2]+1):
        list += (i, j, k)
        if i == list[-6] and j == list[-5] and k == list[-4]:
          list = list[:-3]
  return list


# search for valid combination for total_num McNuggets
def check_combo(list, total_num):
  n = 0
  while (n < (len(list) - 3)):
    if (list[n]*box_size[0] + list[n+1]*box_size[1] + list[n+2]*box_size[2]) == total_num:
      return 1
    else:
      n += 3
  return 0


def main():
  if box_size[0] == 1:
    print 'all sizes possible to buy exactly'
  else:
    for i in range(1, top_lim+1):
      list = make_list(i)
      if check_combo(list, i) == 0:
        combo = 0
        n = i
      else:
        combo += 1
        if combo == box_size[0]:
          break
  print 'Given package sizes', box_size[0], box_size[1], 'and', box_size[2], 'the largest number of McNuggets that cannot be bought in exact quantity is:', n
  return 0        

 

if __name__ == '__main__':
  main()

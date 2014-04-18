#! /usr/bin/python2.5 -tt

# Problem Set 3
# Name: Anna Liu
# Collaborators: N/A
# Time: 00:20:00
# Date: 09/04/2014

# count the number 'key' in the 'target' string.


def countSubStringMatch(target, key):
  location = count = 0
  while location < len(target):
    i = str.find(target, key, location)
    if i >= 0:
      count += 1
      location = (i + len(key))
    else:
      break
  return count


def countSubStringMatchRecursive(target, key):
  count = 0
  i = str.find(target, key)
  if i >= 0:
    target = target[i+len(key):]
    count += 1 + countSubStringMatchRecursive(target, key)
  return count


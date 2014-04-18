#! /usr/bin/python2.5 -tt

# Problem Set 3
# Name: Anna Liu
# Collaborators: N/A
# Time: 00:05:00
# Date: 10/04/2014

# search and return a tuple of starting points of 'key' in 'target'.

def subStringMatchExact(target,key):
  if key == '':
    match = range(0, len(target))
    return match
  match = ()
  location = 0
  while location < len(target):
    i = str.find(target, key, location)
    if i >= 0:
      match += (i,)
      location = (i + len(key))
    else:
      break
  return match



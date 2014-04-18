#! /usr/bin/python2.5 -tt

# Problem Set 3
# Name: Anna Liu
# Collaborators: N/A
# Time: 00:30:00
# Date: 11/04/2014


# returns start points of approximate matches of 'key' in 'target'

import ps3b, ps3c


def subStringMatchExactlyOneSub(target,key):
  
  exactMatch = ps3b.subStringMatchExact(target, key)
  allAnswers = ()
  for miss in range(0,len(key)):
    key1 = key[:miss]
    key2 = key[miss+1:]
    match1 = ps3b.subStringMatchExact(target,key1)
    match2 = ps3b.subStringMatchExact(target,key2)
    filtered = ps3c.constrainedMatchPair(match1,match2,len(key1))
    
    n = 0
    for i in filtered:
      for j in exactMatch:
        if i == j:
          filtered = filtered[:n] + filtered[n+1:]
          n -= 1
      n += 1
      
    allAnswers = allAnswers + filtered
  return allAnswers

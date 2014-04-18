#! /usr/bin/python2.5 -tt

# Problem Set 3
# Name: Anna Liu
# Collaborators: N/A
# Time: 01:00:00
# Date: 11/04/2014

#given starting points for key1, key2 and length of key1
#return start points for 'key1*key2'

import ps3b

def constrainedMatchPair(firstMatch, secondMatch, length):
  match = ()
  n = 0
  for i in firstMatch:
    for j in secondMatch:
      if i+length+1 == j:
        match += (i,)
        n += 1
  return match


def subStringMatchOneSub(key,target):
  allAnswers = ()
  for miss in range(0,len(key)):
    key1 = key[:miss]
    key2 = key[miss+1:]
    match1 = ps3b.subStringMatchExact(target,key1)
    match2 = ps3b.subStringMatchExact(target,key2)
    filtered = constrainedMatchPair(match1,match2,len(key1))
    allAnswers = allAnswers + filtered
  return allAnswers


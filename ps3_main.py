#! /usr/bin/python2.5 -tt

import ps3a, ps3b, ps3c, ps3d


target = 'ATGACATGCACAAGTATGCAT'
key = 'ATG'


def main():

  print ps3a.countSubStringMatch(target, key)
  print ps3a.countSubStringMatchRecursive(target, key)
  print ps3b.subStringMatchExact(target,key)
  
  # for testing constrainedMatchPair(firstMatch, secondMatch, length)
  print ps3c.subStringMatchOneSub(key,target)
  
  print ps3d.subStringMatchExactlyOneSub(target,key)

if __name__ == '__main__':
  main()

#!/usr/bin/env python

import threading
from Queue import Queue
from time import sleep,ctime
import datetime

class Node:

  def __init__(self):
    self.coins = []

  def learning(self,a):
    self.coins.append(a)
    #sleep(0.5)
    for i in range(500000):
      a = 1 + 2**2;



class Hierarchy:
  
  def __init__(self):
    self.nodes = []

    # 8 nodes in a hierarchy
    for i in range(8):
      self.nodes.append(Node())

  def learning(self,sequence):
   for seq in sequence:
     for i in range(8):
       self.nodes[i].learning(seq[i])

if __name__=='__main__':
  starttime = datetime.datetime.now()
  sequence = []
  for i in range(15):
    sequence.append([1,2,3,4,5,6,7,8])
    
  mh = Hierarchy()
  mh.learning(sequence)
  endtime = datetime.datetime.now()
  print endtime-starttime 
  for i in range(8):
    print mh.nodes[i].coins

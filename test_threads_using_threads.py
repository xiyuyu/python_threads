#!/usr/bin/env python

import threading
from Queue import Queue
from time import sleep,ctime
import datetime

class Node(threading.Thread):

  def __init__(self):
    threading.Thread.__init__(self)
    self.learning_queue = Queue()
    self.coins = []

  def send_learning_queue(self,lamda):
    self.learning_queue.put(lamda)
    
  def close_learning(self):
    self.learning_queue.put(None)
    self.learning_queue.join()	  
	  
  def run(self):
    while True:
      lamda = self.learning_queue.get()
      if lamda is None:
        break
        
      self.coins.append(lamda)
      #sleep(0.5)
      
      for i in range(500000):
        a = 1 + 2**2
      
      self.learning_queue.task_done()
    self.learning_queue.task_done()



class Hierarchy:
  
  def __init__(self):
    self.nodes = []

    # 8 nodes in a hierarchy
    for i in range(8):
      self.nodes.append(Node())
      
    for i in range(8):
      self.nodes[i].start()

  def learning(self,sequence):
    for seq in sequence:
      for i in range(8):
        self.nodes[i].send_learning_queue(seq[i])
    for i in range(8):
      self.nodes[i].close_learning()

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

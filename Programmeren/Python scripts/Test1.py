# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 20:42:56 2017

@author: GudjonHelgi
"""

import datetime, threading, time

next_call = time.time()

def foo():
  global next_call
  print (datetime.datetime.now())
  next_call = next_call+1
  threading.Timer( next_call - time.time(), foo ).start()

foo()

# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 11:56:07 2020

@author: Chris Mitchell
"""

import numpy as np

def peakFinder1D(array):
    """Finds and returns a local peak in a one-dimensional array in O(log n)
       time."""
      
    n = len(array)
    if n == 1: return array[0]
    elif n == 2: return [array[0], array[1]][array[0] < array[1]]
    else:
      if array[n // 2] < array[n // 2 - 1]:
        return peakFinder1D(array[:n // 2])
      elif array[n // 2] < array[n // 2 + 1]:
        return peakFinder1D(array[n // 2:])
      else: return array[n // 2]

def peakFinder2D(array):
    """Finds and returns a local peak in a two-dimensional array in O(n log m)
       time. This function takes an numpy array or it can take a two-
       dimensional combinations of lists or tuples."""

    array = np.array(array)
    n, m = array.shape
    if m == 1: return array.max()
    elif m == 2:
        i = array[:,0].argmax()
        return [array[:,0].max(), array[:,1].max()][array[i, 0] < array[i, 1]]
    else:
        i = array[:,m // 2].argmax()
        if array[i, m // 2] < array[i, m // 2 - 1]:
            return peakFinder2D(array[:,:m // 2])
        elif array[i, m // 2] < array[i, m // 2 + 1]:
            return peakFinder2D(array[:,m // 2:])
        else: return array[i, m // 2]

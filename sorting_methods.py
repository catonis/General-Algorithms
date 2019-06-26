# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 22:45:02 2019

@author: Chris Mitchell
"""

def SortInsertion(sortableList):
    """Performs an insertion sort on a list of comparables. Takes a list
    and returns the same list sorted.
    """
    
    sortLen = len(sortableList)
    
    for sortIndex in range(1, sortLen):
        sortKey = sortableList[sortIndex]
        prevIndex = sortIndex - 1
        while prevIndex >= 0 and sortableList[prevIndex] > sortKey:
            sortableList[prevIndex + 1] = sortableList[prevIndex]
            prevIndex = prevIndex - 1
        sortableList[prevIndex + 1] = sortKey
        
    return sortableList


def _SortMergeHorse(sortableList, firstIndex, midIndex, lastIndex):
    
    from math import inf
    
    L = sortableList[firstIndex:midIndex + 1]
    R = sortableList[midIndex + 1:lastIndex + 1]
    L.append(inf)
    R.append(inf)
    
    i = j = 0
    for k in range(firstIndex, lastIndex + 1):
        if L[i] <= R[j]:
            sortableList[k] = L[i]
            i += 1
        else:
            sortableList[k] = R[j]
            j += 1
    

def _SortMergeMain(sortableList, firstIndex, lastIndex):
    """Performs a merge sort on a list of comparables which can be
    subindexed. Returns the sorted array as a list.
    """
        
    if firstIndex < lastIndex:
        middleIndex = (firstIndex + lastIndex) // 2
        _SortMergeMain(sortableList, firstIndex, middleIndex)
        _SortMergeMain(sortableList, middleIndex + 1, lastIndex)
        _SortMergeHorse(sortableList, firstIndex, middleIndex, lastIndex)

def SortMerge(sortableList):
    
    tmpList = sortableList.copy()
    
    _SortMergeMain(tmpList, 0, len(sortableList) - 1)
    
    return tmpList
    

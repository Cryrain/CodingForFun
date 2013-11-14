#! /usr/bin/python
# -*- coding:utf-8 -*-

def quicksort(array,start,end):
    s = start
    e = end
    if s > e:
        return
    key = array[s]
    while s < e:
        while s < e and array[e] >= key:
            e -= 1
        array[s] = array[e]
        while s < e and array[s] <= key:
            s += 1
        if s < e:
            array[e] = array[s]
    array[s] = key

    if s-1>start:
        quicksort(array,start,s-1)
    if s+1 < end:
        quicksort(array,s+1,end)
#输出数组最array最小的N个数
def mininum(array,n):
    if len(array) < n:
        print "N大于数组长度"
    quicksort(array,0,len(array)-1)
    print array[0:n]








if __name__ == "__main__":
    arr = [9,3,1,4,5,2,6,7,10,8,1,2]
    mininum(arr,12)

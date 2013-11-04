#! /usr/bin/python
# -*- coding:utf-8 -*-

# 对字符串按照ascii码排序，然后二分查找字符串2的每一个字母如果有不同
# 就返回false

# 2013.11.3 16:03

def quicksort(array,start,end):
    if(start == end):
        return
    a = start
    b = end
    temp = array[a]

    while a < b:
        while a < b and array[b] >= temp:
            b -= 1
        if a < b:
            array[a] = array[b]
            a += 1
        while a < b and array[a] <= temp:
            a += 1
        if a < b :
            array[b] = array[a]
            b -= 1

    array[a] = temp
    if a > start :
        quicksort(array,start,a-1)
    if a < end :
        quicksort(array,a+1,end)

def binarysearch(array,start,end,key):
    if start > end:
        return -1;
    middle = start + (end-start)/2
    if key < array[middle]:
        return binarysearch(array,start,middle-1,key)
    if key == array[middle]:
        return middle
    if key > array[middle]:
        return binarysearch(array,middle+1,end,key)


def stringcontain(src,query):
    srcarray = []
    queryarray = []
    for c in src :
        srcarray.append(ord(c))
    print srcarray
    for c in query:
        queryarray.append(ord(c))
    quicksort(srcarray,0,len(srcarray)-1)
    for i in queryarray:
        num = binarysearch(srcarray,0,len(srcarray)-1,i)
        if num == -1:
            return False

    return True
        
if __name__ == "__main__":
    arr = [5,3,8,6,0,1,2,3,4]
    print arr
    quicksort(arr,0,len(arr)-1)
    print arr
    num = binarysearch(arr,0,len(arr)-1,2)
    print num
    
    src = "abcdefghijklmnopqrstu"
    query= "abefhlmostx"
    rlt = stringcontain(src,query)
    print rlt
    #quicksort(arr,0,len(arr)-1)

    


#! /usr/bin/python
# -*- coding:utf-8 -*-


# 左旋字符串，最笨的方法，每一次向左移动一次，循环K次
def leftmovestring(array,k):
    n = len(array)
    i = 0
    while i<k:
        temp = array[0]
        for t in range(n-1):
            array[t] = array[t+1]
        array[n-1] = temp
        i += 1
#这个是聪明的办法，时间复杂度o(n)

def leftmovestring2(array,k):
    n = len(array)
    reverse(array,0,k-1)
    reverse(array,k,n-1)
    reverse(array,0,n-1)


def reverse(array,begin,end):
    while begin<end:
        temp = array[begin]
        array[begin] = array[end]
        array[end] = temp
        begin += 1
        end -= 1


if __name__ == '__main__':
    test = 'helloworld'
    arr = list(test)
#    leftmovestring(arr,5)
#    print "".join(arr)
    leftmovestring2(arr,5)
    print ''.join(arr)










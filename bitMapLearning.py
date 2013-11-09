#! /usr/bin/python
# -*- coding:utf-8 -*-

# bitMap 学习
# 所谓的 Bit-map 就是用一个 bit 位来标记某个元素对应的 Value,
# 而 Key 即是该元素。由于采用了 Bit 为单位来存储数据,
# 因此在存储空间方面,可以大大节省。
# 如现在有一个100位的数组，既可以表示1到100，每一位置1
# 具体实现的话，如要表示10000以内的数，则需要申请10000个位，
# 又int型为32位，则要申请 10000/32+1 个int来表示10000个数
#  （C语言）如  数字0   在第一个int的第0位， 24在第24位
#    40 在  第二个int的8位
#  bitmap可以用来对大数据进行去重和排序（必须是不同的数）

#  下面是bitmap的基本实现，包含了可以基本的方法
#  2013年 11月 10日 星期日 01:12:39 CST  By C.R



# 判断一个数在第几个int中

def intcount (num):
#   num 除以 32
    count = num >> 5
    return count
#  判断这个数在对应int的第几个位,把该位数置1，返回值为int

def bitcount(num):
    bitpos = num % 32
    return 0x1 << bitpos
#  在bitmap中将该数对应的位置置1
def setpos1(intarray,num):
    count = intcount(num)
    bitnum = bitcount(num)
    temp = intarray[count]
    bitset = temp | bitnum
    intarray[count] = bitset
#  测试该数对应的bitmap位置是否为1
def test1(intarray,num):
    count = intcount(num)
    bitnum = bitcount(num)
    temp = intarray[count]
    bittest = bitcount(num)
    if temp & bittest != 0:
        return True
    else:
        return False

#  统计一个整数的二进制有有多少个1

def count1(num):
    count = 0
    for i in range(32):
        t = 0x1 << i
        if t & num != 0:
            count += 1
    return count

if __name__ == '__main__':
    intarr = [0]*2
    print bitcount(44)
    print setpos1(intarr,44)
    setpos1(intarr,60)
    print intarr
    print test1(intarr,60)
    print bin(987)
    print count1(987)
    


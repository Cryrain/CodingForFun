#! /usr/bin/python
# -*- coding:utf-8 -*-

#
#   利用位图来检测字符串包含问题，简单快速，时间复杂度O（n+m）
#   定义一个大小为26个字母的数组，先遍历短字符串，若有置1，
#   记下所有1的总数count，
#   遍历长字符串，若对应字母位置为1，则置0，count 减1
#   判断count的值：
#
#
#


def hashcontain(longstr,shortstr):
    hashstring = [0]*26
    count = 0
    for c in shortstr:
        i = ord(c)
        hashstring[i-65] = 1
        count += 1
    for c in longstr:
        if hashstring[ord(c)-65] == 1:
            hashstring[ord(c)-65] = 0
            count -= 1

    if count == 0:
        return True
    else:
        return False



if __name__ == '__main__':
    longstr = 'ABCDFKZGLIOPQWENM'
    shortstr = 'FKPWNZ'

    print hashcontain(longstr,shortstr)



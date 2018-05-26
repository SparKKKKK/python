# _*_ coding:utf-8 _*_
from functools import reduce
print('please input the nummber of quantity')
n = int(input())
print('please input the strings')
L_string=[]
for i in range(n):
    L_string.append(input())
def judge_YN(str):
    L=[]
    L_word = list(str)
    n = len(str)
    for i in range(n):
        if L_word[i] == 'P' or L_word[i] == 'A' or L_word[i] =='T':
            L.append(0)
        else:
            L.append(1)
    a = reduce(lambda x,y:x+y,L)
    if a == 0:
        print('YES')
    else:
        print('NO')
for i in range(n):
    judge_YN(L_string[i])
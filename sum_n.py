# _*_ coding:utf-8 _*_
from functools import reduce
n_str = input()
L_str = list(n_str)
L_num = list(map(int,L_str))
# L_num = []
# for stri in L_str:
#     L_num.append(int(stri))
print(L_num)
# sum_n = 0
# for n in L_num:
    # sum_n = sum_n+n
sum_n = reduce(lambda x,y:x+y,L_num)
print(sum_n)
L_sum = list(map(int,str(sum_n)))
print(L_sum)
d={'yi':1,'er':2,'san':3,'si':4,'wu':5,'liu':6,'qi':7,'ba':8,'jiu':9,'ling':0}
def get_key(dict,value):
    return [k for k,v in dict.items() if v == value]
for i in range(len(L_sum)):
    print(get_key(d,L_sum[i]),end="")
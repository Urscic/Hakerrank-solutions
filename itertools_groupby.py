
from itertools import groupby
string=input()
string=groupby(string)
string=[list(b) for a,b in string]
result=[]
for i in range(len(string)):
    a=[0,0]
    a[0]=(int(string[i][0]))
    a[1]=(len(string[i]))
    print(tuple(a), end=' ')

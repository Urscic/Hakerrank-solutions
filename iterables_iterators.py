from itertools import combinations
n=int(input())
string=input().split()
k=int(input())
tester=[string[i] for i in range(k)]
result=list(combinations(string,k))
length=len(result)
prob=0
for i in range(len(result)):
    if 'a' in result[i]:
        prob+=1
print(round(float(prob/length),4))



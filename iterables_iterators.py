from itertools import combinations
n=9
string='a b c a d b z e o'.split()
k=4
result=list(combinations(string,k))
length=len(result)
prob=0
for i in range(len(result)):
    if 'a' in result[i]:
        prob+=1
print(round(float(prob/length),4))



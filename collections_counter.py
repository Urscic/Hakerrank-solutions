from collections import Counter
x=int(input())
shoes=map(int, input().split())
shoes_list=Counter(shoes)
customers=int(input())
sizes=[]
money=0
for i in range(customers):
    n=list(map(int,(input().split())))
    sizes.append(n)
    n=0
for i in range(len(sizes)):
    number=sizes[i][0]
    if shoes_list[number]!= 0:
        money+=(sizes[i][1])
        shoes_list[number]-=1
    
    else:
        continue

print(money)

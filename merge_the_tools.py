def merge_the_tools(s, k):
    # your code goes here
    length=len(s)
    u=[s[i:(i+k)] for i in range(0,length, k)]
    result=[]
    for i in range(len(u)):
        u_el=u[i]
        result_el=[]
        for j in range(k):
            if j==0:
                result_el.append(u_el[j])
            elif u_el[j-1] not in result_el:
                result_el.append(u_el[j-1])
        result_el=''.join(result_el)
        result.append(result_el)
    print('\n'.join(result))
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

def print_rangoli(size):
    import string
    alphabet=list(string.ascii_lowercase)
    reversed_part=[]
    new_size=size
    flag=0
    for i in range(size*2):
        if i <= size:
            new_size=new_size-1
            if new_size>=0:
                alph1=alphabet[new_size:size] 
                alph1.reverse()
                line_part1="-".join(alph1)
                alph1.reverse()
                line_part2="-".join(alph1[1:])
                if line_part1!='' and line_part2!='':
                    line=line_part1+"-"+line_part2
                elif line_part1!='' or line_part2!='': 
                    line=line_part1+line_part2
                #jeśli line_part !="-", dodajesz line do odwróconej listy
                if line!='-':
                    reversed_part.append(line)
                    print(line.center(size*4-3,'-'))
        else:
            #UWAGA odwrócenie i skrócenie reversed_part NIE MOŻE być w pętli
            if flag==0:
                reversed_part.reverse()
                reversed_part=reversed_part[1:]
                flag=1
            try:
                new_i=i-(size+1)
                print(reversed_part[new_i].center(size*4-3,'-'))
            except:
                continue


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
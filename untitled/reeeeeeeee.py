def reverse_99(s):
    num_list=[]
    for n1 in range(1,s[1]):
        ss=str(s[0]*n1)
        ss=ss[::-1]
        ss=int(ss)
        num_list.append(ss)

    num_list.sort()
    return num_list[len(num_list)-1]

ss=input("두 값 입력 : ")
a=ss.split()
a=[eval(i) for i in a]
print(reverse_99(a))
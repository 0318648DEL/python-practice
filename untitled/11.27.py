def sortColumns(m):
    s=[]
    tc=[]
    tr=[]
    tt=[]
    for c in range(len(m)):
        for i in range(len(m)):
            tc.append(m[i][c])
        tc.sort()
        tt.append(tc)
        tc=[]
    for c in range(len(tt)):
        for i in range(len(tt)):
            tr.append(tt[i][c])
        s.append(tr)
        tr=[]
    return s

r1=input("3x3 행렬을 한 행씩 입력하세요 : \n")
r2=input()
r3=input()

l1 = r1.split()
l2 = r2.split()
l3 = r3.split()

l1 = [eval(i) for i in l1]
l2 = [eval(i) for i in l2]
l3 = [eval(i) for i in l3]
m = [l1, l2, l3]
m=sortColumns(m)
print("열 정렬된 리스트는 다음과 같습니다. : ")
for r in m:
    for i in r:
        print(i,end="   ")
    print()
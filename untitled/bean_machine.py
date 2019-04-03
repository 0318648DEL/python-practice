import random

B=eval(input("떨어트릴 공의 갯수를 입력하세요. : "))
N=eval(input("콩 기계의 슬롯 개수를 입력하세요. : "))

slots=[0]*N

for i in range(B):
    NofR=0
    s=""
    for j in range(N-1):
        if random.randint(0,1)==1:
            NofR+=1
            s=s+"R"
        else:
            s=s+"L"
    print(s)
    slots[NofR]+=1
l=slots[:]
l.sort()
Max=l[-1]#콩 막대그래프 중에서 제일 긴 값
#히스토그램 그리기
for h in range(Max,0,-1): #h = Max, Max-1, .....
    for s in slots:
        if s>=h:
            print("0",end="")
        else:
            print(" ",end="")
    print()


import random
number=[0]*4
for i in range(1000000):
    x=random.random()*2-1 #random.random() [0,1)실수 생성 [-1,1)
    y=random.random()*2-1
    if x<0:
        number[0]+=1
    elif y<0:
        number[3]+=1
    else:
        y1=-x+1
        if y<y1:
            number[2]+=1
        else:
            number[1]+=1

for f in range(0,4):
    if not (f+1)%2==0:
        print("{0} 번째 영역엔 {1}만큼 꽂혔다.".format(f+1,number[f]))

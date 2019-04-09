s=input("정수를 입력하세요 : ")
l=s.split()
l=[eval(i) for i in l]
avr=0
high=0
low=0

for i in range(0,len(l)):
   avr+=l[i]
avr=avr/len(l)

for i in range(0,len(l)):
    if l[i]>avr:
        high+=1
    elif l[i]<avr:
        low+=1

print("평균 이상 갯수 : {0}, 평균 이하 갯수 : {1}".format(high,low))
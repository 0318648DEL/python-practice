s=input("정수를 입력하세요 : ")
l=s.split()#자동 리스트 작성
l=[eval(i) for i in l]#list comprehension
max=0
l.sort()
for i in range(0,l[-1]):
    if l.count(i)>=max:
        max=l.count(i)

for i in range(0,l[-1]):
    if l.count(i)==max:
        print("가장 많이 나온 숫자는 : {0}".format(i))
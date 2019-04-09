s=input("1과 100 사이의 정수를 입력하세요 : ")
l=s.split()#자동 리스트 작성
l=[eval(i) for i in l]#list comprehension

#for i in range(len(l)-1,-1,-1): #n-1,n-2,....0
#    print(l[i])

for i in range(1,101,1):
    if l.count(i)>=1:
        print("{0}-{1}번 나타남.".format(i,l.count(i)))
s=input("정수를 입력하세요 : ")
l=s.split()
l=[eval(i) for i in l]

l.reverse()

print(l)
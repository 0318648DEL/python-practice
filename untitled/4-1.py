from math import *
a,b,c=eval(input("a,b,c를 입력하세요 : "))
p=b**2-(4*a*c)
r1=(-1*b+(b**2-(4*a*c))**0.5)/(2*a)
r2=(-1*b-(b**2-(4*a*c))**0.5)/(2*a)

if p>0:
    if r1==r2:
        print("실근은 {0} 입니다.".format(r1))
    else:
        print("실근은 {0}과 {1} 입니다.".format(r1,r2))
else:
    print("이 방정식은 실근이 존재하지 않습니다.")
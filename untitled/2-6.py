n=eval(input("0과 1000사이의 숫자 입력 : "))
while n>1000:
    n = eval(input("0과 1000사이의 숫자 입력 : "))

sum=0
while n>0:
    sum+=n%10
    n=n//10

print("각 자리의 숫자의 합 : ",sum)

'''
r=0
while n>0:
    r=r*10+n%10
    n=n//10

'''
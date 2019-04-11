def gcd(m,n):
    if m%n==0:
        return n
    else:
        return gcd(n,m%n)


m,n=eval(input("두 정수를 입력해주세요 : "))
print("최대 공약수는 : ",gcd(m,n))
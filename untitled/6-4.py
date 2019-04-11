def rev(number):
    r=str(number)
    r=r[::-1]
    r=int(r)
    return r

i=eval(input("역을 반환할 값을 입력하세요 : "))
print("역 : ",rev(i))
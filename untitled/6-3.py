def rev(number):
    r=str(number)
    r=r[::-1]
    r=int(r)
    return r

def isPalindrome(number):
    r=number
    if number==rev(r):
        return True
    else:
        return False

i=eval(input("역을 반환할 값을 입력하세요 : "))
print("역 : ",rev(i))
checkk=eval(input("대칭수인지 확인할 값을 입력하세요 : "))
print(isPalindrome(checkk))

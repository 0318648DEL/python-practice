def displaySortedNumbers(num1,num2,num3):
    list_unsort=[num1,num2,num3]
    list_unsort.sort()
    return list_unsort

num1,num2,num3=eval(input("세 개의 수를 입력하세요 : "))
print("정렬된 숫자는 " , ",".join(map(str,displaySortedNumbers(num1,num2,num3))),"입니다")
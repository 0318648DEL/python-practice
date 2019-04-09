def indexOfSmallestElement(lst):
    min=0
    for i in range(1,len(lst)):
        if lst[min]>lst[i]:
            min=i
    return min

s=input("정수들을 공란으로 분리해서 입력 : ")
lst=s.split()
lst=[eval(i) for i in lst]
print("가장 작은 원소의 인덱스는 ",indexOfSmallestElement(lst))
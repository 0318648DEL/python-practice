def isSorted(lst):
    t=0
    for i in range(0,len(lst)-1):
        if lst[i]>lst[i+1]:
            t=1
            break
    if t==1:
        print("리스트는 정렬되어 있지 않습니다.")

e=input("리스트를 입력하세요 : ")
lst=e.split()
lst=[eval(i) for i in lst]
isSorted(lst)
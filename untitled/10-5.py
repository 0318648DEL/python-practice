num=input("10개의 숫자를 입력하세요 : ")
list1=num.split()
list1=[eval(i) for i in list1]
list2=[]
for i in range(0,len(list1)):
    if not list1[i] in list2:
        list2.append(list1[i])


print("중복을 제거한 고유한 숫자 : ",list2)
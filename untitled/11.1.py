def sumColumn(m,columnIndex):
    return m[0][columnIndex]+m[1][columnIndex]+m[2][columnIndex]

r1=input("3x4 행렬의 행 0번에 대한 원소를 입력하세요 : ")
r2=input("3x4 행렬의 행 1번에 대한 원소를 입력하세요 : ")
r3=input("3x4 행렬의 행 2번에 대한 원소를 입력하세요 : ")

l1=r1.split()
l2=r2.split()
l3=r3.split()

l1=[eval(i) for i in l1]
l2=[eval(i) for i in l2]
l3=[eval(i) for i in l3]
m=[l1,l2,l3]

print("열 0번 원소의 총 합은 {0} 입니다.".format(sumColumn(m,0)))
print("열 0번 원소의 총 합은 {0} 입니다.".format(sumColumn(m,1)))
print("열 0번 원소의 총 합은 {0} 입니다.".format(sumColumn(m,2)))
print("열 0번 원소의 총 합은 {0} 입니다.".format(sumColumn(m,3)))
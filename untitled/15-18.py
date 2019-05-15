num =0

def hanoi(ndisks,startPeg=1,endPeg=3):
	global num
	if ndisks:
		hanoi(ndisks-1,startPeg,6-startPeg-endPeg)
		print(startPeg,"번 기둥의",ndisks,"빈 원반을",endPeg,"번 기둥에 옯깁니다.")
		num+=1
		hanoi(ndisks-1,6-startPeg-endPeg,endPeg)

n=eval(input("갯수를 입력하세요. : "))
hanoi(10)
print("필요한 디스크 이동 횟수는 {0}입니다.".format(num))
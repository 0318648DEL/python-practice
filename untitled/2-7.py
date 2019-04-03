minute=eval(input("분에 대한 숫자를 입력하세요 : "))

years=minute//(60*24*365)
days=(minute%(60*24*365))//(60*24)

print(minute,"분은 약",years,"년 ",days,"일 입니다.")
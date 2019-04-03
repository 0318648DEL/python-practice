g=eval(input("약정금액 : "))
yr=eval(input("년이율 : "))
t=eval(input("약정기간 : "))
money=g/((1+yr/1200)**(t*12))

print("월 납입금은 ",money,"입니다")
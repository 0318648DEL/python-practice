name=input("사원 이름을 입력하세요 : ")
work_hour=eval(input("주 당 근무시간을 입력하세요 : "))
pay=eval(input("시간 당 급여를 입력하세요 : "))
nor_tax=eval(input("원천징수세율을 입력하세요 : "))
civ_tax=eval(input("지방세율을 입력하세요 : "))
total=pay*work_hour

print("사원 이름 : ",name)
print("주당 근무시간 : ",work_hour)
print("임금 : ",pay)
print("총 급여 : ",total)
print("공제 : \n\t원천 징수세({0}%) : {1}\n\t주민세({2}%) : {3}\n\t총 공제 : {4}\n공제 후 급여 : {5}".
      format(nor_tax*100,nor_tax*total,civ_tax*100,civ_tax*total,nor_tax*total+civ_tax*total,total-(nor_tax*total+civ_tax*total)))

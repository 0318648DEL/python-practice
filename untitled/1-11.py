year=31536000
born=year//7
death=year//13
mig=year//45
people=312032486

for i in [1,2,3,4,5]:
    print(i*5,"년 후 인구수 : ",people+5*i*(born-death+mig))
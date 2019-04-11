def add(i):
    if i==1:
        return 1/2
    return i/(i+1)+add(i-1)

for i in range(1,21,1): #[1,2,3,4,5,6,7,8.9.10}
    print("m({0})={1}".format(i,add(i)))
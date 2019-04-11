d=5000000
def find(total):
    comm=total-d
    if comm<=400000:
        sold=comm*12.5
    elif 400001<=comm<=1000000:
        sold=comm*10
    elif comm>=1000001:
        sold=comm*(100/12)
    return sold

print("매출액 : {0:.2f}".format(find(30000000)))